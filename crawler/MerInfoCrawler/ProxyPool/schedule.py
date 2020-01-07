import time
from multiprocessing import Process
import asyncio
import aiohttp
from ProxyPool.setting import *
from asyncio import TimeoutError
from aiohttp import ClientConnectionError
from ProxyPool.erro import ResourceDepletionError
from ProxyPool.getting import ProxyGetting
from ProxyPool.mongoDB import mongoDB

class Valid_Test(object):
    def __init__(self):
        self._raw_proxies=None
        self._useful_proxies=[]
    def set_raw_proxies(self,proxies):
        self._raw_proxies=proxies
        self._connection=mongoDB()
    async def test_proxy(self,proxy):
        try:
            async with aiohttp.ClientSession() as session:
                try:
                    if isinstance(proxy,bytes):
                        proxy=proxy.decode('utf-8')
                    real_proxy='http://'+proxy
                    print("正在测试： ",proxy)
                    async  with session.get(TEST_API,proxy=real_proxy,timeout=get_proxy_timeout) as response:
                        if response.status==200:
                            self._connection.put(proxy)
                            print("可用IP：",proxy)
                except (ClientConnectionError,TimeoutError,ValueError):
                    print("不可用IP：",proxy)
        except ClientConnectionError as e:
            print(e)
            pass
    def test(self):
        try:
            loop = asyncio.get_event_loop()
            tasks=[self.test_proxy(proxy) for proxy in self._raw_proxies]
            loop.run_until_complete(asyncio.wait(tasks))
        except ValueError:
            print("异步检测错误！")


class add_Proxies(object):
    def __init__(self,proxynum):
        self._proxynum=proxynum
        self._connection=mongoDB()
        self._test=Valid_Test()
        self._crawler=ProxyGetting()
    def is_over_proxynum(self):
        if self._connection.queue_len> self._proxynum:
            return True
        else:
            return False
    def add_to_queue(self):
        proxy_count=0
        while not self.is_over_proxynum():
            raw_proxies = list(self._crawler.get_raw_proxies())
            self._test.set_raw_proxies(raw_proxies)
            self._test.test()
            proxy_count += len(raw_proxies)
            if self.is_over_proxynum():
                print("IP数量已经足够！")
                break
            if proxy_count==0:
                raise ResourceDepletionError
        self._test.set_raw_proxies(raw_proxies)
        self._test.test()
        proxy_count += len(raw_proxies)




class Schedule(object):
    @staticmethod
    def vaild_proxy(cycle=VALID_CHECK_CYCLE):
        connection=mongoDB()
        test=Valid_Test()
        while True:
            print("刷新IP：")
            count = int(0.5*connection.queue_len)
            if count==0:
                print("等待添加IP...")
                time.sleep(cycle)
                continue
            raw_proxies=connection.get(count)
            test.set_raw_proxies(raw_proxies)
            test.test()
            time.sleep(cycle)
    @staticmethod
    def check_pool(lower_proxynum=POOL_LOWER_PROXYNUM,upper_proxynum=POOL_UPPER_PROXYNUM,cycle=POOL_LEN_CHECK_CYCLE):
        connection=mongoDB()
        adder=add_Proxies(upper_proxynum)
        while True:
            if connection.queue_len<lower_proxynum:
                adder.add_to_queue()
            time.sleep(cycle)
    def run(self):
        print("IP进程正在运行...")
        valid_process=Process(target=Schedule.vaild_proxy)
        check_process=Process(target=Schedule.check_pool)
        valid_process.start()
        check_process.start()
