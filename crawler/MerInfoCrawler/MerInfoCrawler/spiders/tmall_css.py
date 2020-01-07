# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider,Request
from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.support.ui import WebDriverWait
from MerInfoCrawler.items import TmallItem
import time
class TaobaoSpider(Spider):
    name = 'tmall_css'
    allowed_domains = ['www.taobao.com']
    #url = 'https://list.tmall.com/search_product.htm?q=黄金'


    def __init__(self):
        SERVICE_ARGS = ['--load-images=false','--disk-cache=true','--ignore-ssl-errors=true']
        self.broswer=webdriver.PhantomJS(service_args=SERVICE_ARGS)
        #chrome_option=webdriver.ChromeOptions()
        #chrome_option.add_argument('--proxy-server=127.0.0.1:6023')
        #self.broswer=webdriver.Chrome()
        self.broswer.set_page_load_timeout(30)
        #self.wait = WebDriverWait(self.broswer,30)
    def closed(self,spider):
        self.broswer.close()

    def start_requests(self):
        url_css =  'https://list.tmall.com/search_product.htm?q=周生生黄金'
        yield Request(url=url_css, callback=self.parse)
    def parse(self, response):
        html = self.broswer.page_source
        doc = pq(html)
        products = doc('#J_ItemList .product .product-iWrap').items()

        for product in products:
            item=TmallItem()
            item['source'] = 'tmall'
            item['name']=product.find('.productTitle').text()
            item['price']=product.find('.productPrice').text()
            item['shop']=product.find('.productShop').text()
            item['date'] = time.strftime('%Y.%m.%d', time.localtime(time.time()))
            item['url'] ='https:' + product.find('.productImg-wrap a').attr('href')
            yield item