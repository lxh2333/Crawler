import pymongo
import re
from ProxyPool.erro import PoolEmptyError
from ProxyPool.setting import MONGO_TABLE,MONGO_URL,MONGO_DB
class mongoDB(object):
    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]

    def put(self,proxy):
        proxies = {'proxy':proxy}
        self.db[MONGO_TABLE].insert(dict(proxies))

    def get(self,count=1):
        table =self.db[MONGO_TABLE]
        proxies = []
        proxy = list(table.find())
        for i in range(count):
            proxy_1 = proxy[i]
            proxies.append(proxy_1['proxy'])
            table.delete_one(proxy_1)
        return proxies
    def pop(self):
        try:
            table = self.db[MONGO_TABLE]
            proxies = list(table.find())
            count = table.count()
            proxy = proxies[count-1]
            table.delete_one(proxy)
            return proxy['proxy']
        except:
            raise PoolEmptyError

    @property
    def queue_len(self):
        table = self.db[MONGO_TABLE]
        return table.count()