# -*- coding: utf-8 -*-
import re

import scrapy
import pymongo
import pandas as pd
from scrapy import Spider,Request
from pyquery import PyQuery as pq
from MerInfoCrawler.items import TaoBaoItem
from TaobaoCookies.config import MONGO_TABLE,MONGO_DB,MONGO_URL
import time

def acquire_from_mongo():
    client = pymongo.MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    table = db[MONGO_TABLE]
    count = table.count()
    cookies = list(table.find())
    cookie = cookies[count - 1]
    print(cookie)
    return cookie
class Taobao2Spider(scrapy.Spider):
    name = 'taobao'

    def start_requests(self):
        start_urls = ['https://s.taobao.com/search?q=黄金',
                      'https://s.taobao.com/search?q=%E9%BB%84%E9%87%91&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44']
        header = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1;Trident/5.0)',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8', }
        cookie=acquire_from_mongo()
        for url in start_urls:
            yield Request(url=url, callback=self.parse,headers=header,cookies=cookie)
    def parse(self, response):
        titles = re.findall(r'"raw_title":"([^"]+)"', response.text, re.I)
        prices = re.findall(r'"view_price":"([^"]+)"', response.text, re.I)
        shops = re.findall(r'"nick":"([^"]+)"', response.text, re.I)
        i_title = 0
        for title in titles:
            i_title += 1
        print(prices)
        print()
        for i in range(i_title):
            item = TaoBaoItem()
            item['source'] = 'taobao'
            item['name'] = titles[i]
            item['price'] = prices[i]
            item['shop'] = shops[i]
            item['date'] = time.strftime('%Y.%m.%d', time.localtime(time.time()))
            yield item
