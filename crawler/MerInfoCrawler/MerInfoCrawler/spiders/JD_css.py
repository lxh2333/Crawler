# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from selenium import webdriver
from pyquery import PyQuery as pq
from MerInfoCrawler.items import JDItem
import time
class JdSpider(Spider):
    name = 'JD_css'
    allowed_domains = ['www.jd.com']
    #custom_settings = {
        #'LOG_LEVEL': 'INFO',
    #}

    def __init__(self):
        SERVICE_ARGS = ['--load-images=false','--disk-cache=true','--ignore-ssl-errors=true']
        self.broswer=webdriver.PhantomJS(service_args=SERVICE_ARGS)
        self.broswer.set_page_load_timeout(30)
    def closed(self,spider):
        self.broswer.close()
    def start_requests(self):
        url_css =  'https://search.jd.com/Search?keyword=%E5%91%A8%E7%94%9F%E7%94%9F%E9%BB%84%E9%87%91&enc=utf-8&wq=%E5%91%A8%E7%94%9F%E7%94%9F%E9%BB%84%E9%87%91'
        yield Request(url=url_css,callback=self.parse)
    def parse(self, response):
        html = self.broswer.page_source
        doc = pq(html)
        products = doc('#J_goodsList .gl-item .gl-i-wrap').items()
        for product in products:
            item = JDItem()
            item['source']='jd'
            item['name']=product.find('.p-name').text()
            item['price']=product.find('.p-price').text()
            item['shop']=product.find('.p-shop').text()
            item['date'] = time.strftime('%Y.%m.%d',time.localtime(time.time()))
            item['url'] ='https:' + product.find('.p-img a').attr('href')
            yield item
