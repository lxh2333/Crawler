# -*- coding: utf-8 -*-
import json
import re
from os.path import join
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from scrapy import Spider,Request

from MerInfoCrawler.items import SgeItem,SgeJrhqItem


class SgeSpider(Spider):
    name = 'sge'
    allowed_domains = ['www.sge.com.cn']
    start_urls = ['https://www.sge.com.cn/']
    new_url = 'https://www.sge.com.cn'
    #custom_settings = {
        #'LOG_LEVEL':'INFO',
    #}

    def start_requests(self):
        url = 'https://www.sge.com.cn/sjzx/mrhqsj/'
        yield Request(url,callback=self.parse,dont_filter=True)
        url_jrhq = 'https://www.sge.com.cn/sjzx/yshqbg'
        yield Request(url=url_jrhq,callback=self.parse_jrhq)

    def parse(self, response):
        id=response.xpath('//li').re('<a.*?href="(.*?)" class="title.*?>')
        for i in range(len(id)):
            yield Request(url=self.new_url+id[i],callback=self.parse_data,dont_filter=True)
    def parse_data(self,response):
        date=response.xpath('//span').re('<i>时间:</i>(.*?)</span>')
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        trs = soup.findAll('tr')
        AuList = []
        PGC = 0
        Ag99 = 0
        for tr in trs:
            Au = []
            for td in tr:
                if td.string.strip() == '':
                    pass
                else:
                    Au.append(td.string.strip())
            AuList.append(Au)
        item =SgeItem()
        item['source']='sge'
        item['date']=date[0]
        for i in range(1,len(trs)):
            if AuList[i][0]=='Au99.95':
                item['Au95'] = AuList[i][1]+'/'+AuList[i][4]+'/'+AuList[i][5]+'/'+AuList[i][6]+'/'+AuList[i][7]
            elif AuList[i][0]=='Au99.99':
                item['Au99'] = AuList[i][1]+'/'+AuList[i][4]+'/'+AuList[i][5]+'/'+AuList[i][6]+'/'+AuList[i][7]
            elif AuList[i][0]=='Au100'or AuList[i][0]=='Au100g':
                item['Au100'] =AuList[i][1]+'/'+AuList[i][4]+'/'+AuList[i][5]+'/'+AuList[i][6]+'/'+AuList[i][7]
            elif AuList[i][0]=='iAu99.99':
                item['iAu99'] = AuList[i][1]+'/'+AuList[i][4]+'/'+AuList[i][5]+'/'+AuList[i][6]+'/'+AuList[i][7]
            elif AuList[i][0]=='Au(T+D)':
                item['AuTD'] = AuList[i][1]+'/'+AuList[i][4]+'/'+AuList[i][5]+'/'+AuList[i][6]+'/'+AuList[i][7]
            elif AuList[i][0]=='Au(T+N1)':
                item['AuTN1'] = AuList[i][1]+'/'+AuList[i][4]+'/'+AuList[i][5]+'/'+AuList[i][6]+'/'+AuList[i][7]
            elif AuList[i][0]=='Au(T+N2)':
                item['AuTN2'] = AuList[i][1]+'/'+AuList[i][4]+'/'+AuList[i][5]+'/'+AuList[i][6]+'/'+AuList[i][7]
            elif AuList[i][0]=='mAu(T+D)':
                item['mAuTD'] = AuList[i][1]+'/'+AuList[i][4]+'/'+AuList[i][5]+'/'+AuList[i][6]+'/'+AuList[i][7]
            elif AuList[i][0]=='Pt99.95':
                item['Pt95'] = AuList[i][1]+'/'+AuList[i][4]+'/'+AuList[i][5]+'/'+AuList[i][6]+'/'+AuList[i][7]
            elif AuList[i][0]=='Ag99.99':
                item['Ag99'] = AuList[i][1]+'/'+AuList[i][4]+'/'+AuList[i][5]+'/'+AuList[i][6]+'/'+AuList[i][7]
                Ag99=1
            elif AuList[i][0]=='Ag(T+D)':
                item['AgTD'] = AuList[i][1]+'/'+AuList[i][4]+'/'+AuList[i][5]+'/'+AuList[i][6]+'/'+AuList[i][7]
            elif AuList[i][0]=='PGC30g' or AuList[i][0]=='熊猫金币30g':
                item['PGC'] = AuList[i][1]+'/'+AuList[i][4]+'/'+AuList[i][5]+'/'+AuList[i][6]+'/'+AuList[i][7]
                PGC=1
        if len(trs) < 13:
            if Ag99==1 and PGC==0:
                item['PGC'] = '-'
            if PGC==1 and Ag99==0:
                item['Ag99'] = '-'
            if PGC==0 and Ag99==0:
                item['PGC'] = '-'
                item['Ag99'] = '-'
        yield item
    def parse_jrhq(self,response):
        title = response.xpath('//div').re('<h1>(.*?)</h1>')
        date = response.xpath('//span').re('<i>时间:</i>(.*?)</span>')
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        trs = soup.findAll('tr')
        AuList_jrhq = []
        for tr in trs:
            Au = []
            for td in tr:
                if td.string.strip() == '':
                    pass
                else:
                    Au.append(td.string.strip())
            AuList_jrhq.append(Au)
        item = SgeJrhqItem()
        item['title'] = title[0]
        item['date'] = date[0]
        for i in range(1,len(trs)):
            if AuList_jrhq[i][0]=='Au99.95':
                item['Au95'] = AuList_jrhq[i][1]+'-'+AuList_jrhq[i][2]+'-'+AuList_jrhq[i][3]+'-'+AuList_jrhq[i][4]
            elif AuList_jrhq[i][0]=='Au99.99':
                item['Au99'] = AuList_jrhq[i][1]+'-'+AuList_jrhq[i][2]+'-'+AuList_jrhq[i][3]+'-'+AuList_jrhq[i][4]
            elif AuList_jrhq[i][0]=='Au100'or AuList_jrhq[i][0]=='Au100g':
                item['Au100'] = AuList_jrhq[i][1]+'-'+AuList_jrhq[i][2]+'-'+AuList_jrhq[i][3]+'-'+AuList_jrhq[i][4]
            elif AuList_jrhq[i][0]=='iAu99.99':
                item['iAu99'] = AuList_jrhq[i][1]+'-'+AuList_jrhq[i][2]+'-'+AuList_jrhq[i][3]+'-'+AuList_jrhq[i][4]
            elif AuList_jrhq[i][0]=='Au(T+D)':
                item['AuTD'] = AuList_jrhq[i][1]+'-'+AuList_jrhq[i][2]+'-'+AuList_jrhq[i][3]+'-'+AuList_jrhq[i][4]
            elif AuList_jrhq[i][0]=='Au(T+N1)':
                item['AuTN1'] = AuList_jrhq[i][1]+'-'+AuList_jrhq[i][2]+'-'+AuList_jrhq[i][3]+'-'+AuList_jrhq[i][4]
            elif AuList_jrhq[i][0]=='Au(T+N2)':
                item['AuTN2'] = AuList_jrhq[i][1]+'-'+AuList_jrhq[i][2]+'-'+AuList_jrhq[i][3]+'-'+AuList_jrhq[i][4]
            elif AuList_jrhq[i][0]=='mAu(T+D)':
                item['mAuTD'] = AuList_jrhq[i][1]+'-'+AuList_jrhq[i][2]+'-'+AuList_jrhq[i][3]+'-'+AuList_jrhq[i][4]
            elif AuList_jrhq[i][0]=='Pt99.95':
                item['Pt95'] = AuList_jrhq[i][1]+'-'+AuList_jrhq[i][2]+'-'+AuList_jrhq[i][3]+'-'+AuList_jrhq[i][4]
            elif AuList_jrhq[i][0]=='Ag99.99':
                item['Ag99'] = AuList_jrhq[i][1]+'-'+AuList_jrhq[i][2]+'-'+AuList_jrhq[i][3]+'-'+AuList_jrhq[i][4]
            elif AuList_jrhq[i][0]=='Ag(T+D)':
                item['AgTD'] = AuList_jrhq[i][1]+'-'+AuList_jrhq[i][2]+'-'+AuList_jrhq[i][3]+'-'+AuList_jrhq[i][4]
            elif AuList_jrhq[i][0]=='PGC30g' or AuList_jrhq[i][0]=='熊猫金币30g':
                item['PGC'] = AuList_jrhq[i][1]+'-'+AuList_jrhq[i][2]+'-'+AuList_jrhq[i][3]+'-'+AuList_jrhq[i][4]
        yield item