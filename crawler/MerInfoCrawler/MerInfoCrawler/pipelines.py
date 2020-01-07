# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import re

import pymongo
from MerInfoCrawler.items import SgeItem,JDItem,TaoBaoItem,JDInfoItem,TmallInfoItem,SgeJrhqItem,TmallItem

class ItemsPipeline(object):
    def process_item(self,item,spider):
        if isinstance(item, SgeItem):
            if not item['Ag99'] == '-':
                if re.match('\d+,\d+',item['Ag99']):
                    num = re.split(r',',item['Ag99'])
                    item['Ag99']=num[0]+num[1]+num[2]+num[3]
            if not item['AgTD'] == '-':
                if re.match('\d+,\d+',item['AgTD']):
                    num = re.split(r',',item['AgTD'])
                    item['AgTD']=num[0]+num[1]+num[2]+num[3]
            return item
        if isinstance(item, SgeJrhqItem):
            return item
        if isinstance(item, JDItem):
            if item['price']:
                if re.match('￥\d+￥\d+',item['price']):
                    price = re.split(r'￥',item['price'])
                    item['price'] = price[1]
                elif re.match('¥\d+¥\d+',item['price']):
                    price = re.split(r'¥', item['price'])
                    item['price'] = price[1]
                else:
                    item['price'] = item['price'][1:]
            return item
        if isinstance(item, JDInfoItem):
            return item
        if isinstance(item, TaoBaoItem):
            if item['price'][0]=='¥' or item['price'][0]=='￥':
                item['price'] = item['price'][1:]
            return item
        if isinstance(item, TmallItem):
            if item['price'][0]=='¥' or item['price'][0]=='￥':
                item['price'] = item['price'][1:]
            return item
        if isinstance(item, TmallInfoItem):
            return item

class MongoPipeline(object):
    def __init__(self,mongo_url,mongo_db,checkFile):
        self.mongo_url=mongo_url
        self.mongo_db=mongo_db
        self.checkFile=checkFile

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            checkFile=crawler.settings.get('CHECK_FILE')
        )
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db =self.client[self.mongo_db]
        f = open(self.checkFile,"w")
        f.close()
    def process_item(self,item,spider):
        if isinstance(item,SgeItem):
            self.db['sgeprice'].update({'date':item['date']},{'$set':item},True)
            return item
        elif isinstance(item, SgeJrhqItem):
            self.db['sgejrhq'].insert(dict(item))
        elif isinstance(item,JDItem):
            #self.db['jdprice'].update({'date':item['date']},{'$set':item},True)
            self.db['jdprice'].insert(dict(item))
            return item
        elif isinstance(item,JDInfoItem):
            self.db['jdinfo'].insert(dict(item))
            return item
        elif isinstance(item,TaoBaoItem):
            self.db['tbprice'].update({'url': item['url']}, {'$set': item}, True)
            #self.db['tbprice'].insert(dict(item))
            return item
        elif isinstance(item,TmallItem):
            #self.db['tmallprice'].update({'url': item['url']}, {'$set': item}, True)
            self.db['tmallprice'].insert(dict(item))
            return item
        elif isinstance(item,TmallInfoItem):
            self.db['tmallinfo'].insert(dict(item))
            return item
    def close_spider(self,spider):
        self.client.close()
        isFieldExit = os.path.isfile(self.checkFile)
        if isFieldExit:
            os.remove(self.checkFile)