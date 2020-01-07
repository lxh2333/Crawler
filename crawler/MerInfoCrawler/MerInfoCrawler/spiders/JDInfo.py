import time
from scrapy import Spider,Request
from selenium import webdriver
from pyquery import PyQuery as pq
from MerInfoCrawler.items import JDInfoItem
class JDInfoSpider(Spider):
    name = 'JD_Info'
    start_urls = []
    def __init__(self):
        SERVICE_ARGS = ['--load-images=false','--disk-cache=true','--ignore-ssl-errors=true']
        self.broswer=webdriver.PhantomJS(service_args=SERVICE_ARGS)
        self.broswer.set_page_load_timeout(30)
    def closed(self,spider):
        self.broswer.close()
    def start_requests(self):
        url_css = 'https://mall.jd.com/index-31701.html'
        yield Request(url=url_css, callback=self.parse_css)
        url_ctf = 'https://mall.jd.com/index-1000085470.html'
        yield Request(url=url_ctf, callback=self.parse_ctf)
    def parse_css(self, response):
        info = response.xpath('//li').re('<li class="floatl" style="margin-left.*?>(.*?)</li>')
        item = JDInfoItem()
        item['shop'] = '周生生'
        item['date'] = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        item['info'] = info
        return item
    def parse_ctf(self, response):
        html = self.broswer.page_source
        doc = pq(html)
        info = doc('.usergoldprice ul li').text()
        item = JDInfoItem()
        item['shop'] = '周大福'
        item['date'] = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        item['info'] = info
        return item