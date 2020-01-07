import time
from scrapy import Spider,Request
from selenium import webdriver
from pyquery import PyQuery as pq
from MerInfoCrawler.items import TmallInfoItem
class TmallInfoSpider(Spider):
    name = 'TmallInfo'
    start_urls = []
    def __init__(self):
        SERVICE_ARGS = ['--load-images=false','--disk-cache=true','--ignore-ssl-errors=true']
        self.broswer=webdriver.PhantomJS(service_args=SERVICE_ARGS)
        self.broswer.set_page_load_timeout(30)
    def closed(self,spider):
        self.broswer.close()
    def start_requests(self):
        url_css ='https://chowsangsang.tmall.com/'
        yield Request(url=url_css,callback=self.parse_css)
        url_ctf = 'https://ctf.tmall.com'
        yield Request(url=url_ctf, callback=self.parse_ctf)

    def parse_css(self, response):
        info = response.xpath('//li').re('<li class="floatl" style="margin-left.*?>(.*?)</li>')
        item = TmallInfoItem()
        item['shop'] = '周生生'
        item['date'] = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        item['info'] = info[0]+' '+info[1]+' '+info[2]+' '+info[3]
        return item

    def parse_ctf(self, response):
        html = self.broswer.page_source
        doc = pq(html)
        info = doc('.goldprice ul li').text()
        item = TmallInfoItem()
        item['shop'] = '周大福'
        item['date'] = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        item['info'] = info
        return item