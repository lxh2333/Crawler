# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import requests
from bs4 import BeautifulSoup
from scrapy import signals
from ProxyPool.Queue import Queue
from ProxyPool.Redis import RedisDB
from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException
import time

class MerinfocrawlerSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MerinfocrawlerDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class HttpProxyMiddleware(object):
    def process_request(self, request, spider):
        #queue=Queue()
        #proxy=queue.pop()
        conn=RedisDB()
        proxy=conn.pop()
        request.meta['proxy'] = 'http://' + proxy
class  SeleniumMiddleware(object):
    def process_request(self,request,spider):
        if spider.name=='JD_css' or spider.name=='JD_ctf':
            try:
                spider.broswer.get(request.url)
                spider.broswer.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            except TimeoutException as e:
                print("超时")
                spider.broswer.execute_script('window.stop()')
            time.sleep(2)
            return HtmlResponse(url=request.url,body=spider.broswer.page_source,
                                encoding="utf-8",request=request)
        if spider.name=='JD_Info':
            try:
                spider.broswer.get(request.url)
                time.sleep(2)
                spider.broswer.execute_script('window.scrollTo(0,11700)')
            except TimeoutException as e:
                print("超时")
            return HtmlResponse(url=request.url,body=spider.broswer.page_source,
                                encoding="utf-8",request=request)
        if spider.name=='tmall_css' or spider.name=='tmall_ctf':
            try:
                spider.broswer.get(request.url)
            except TimeoutException:
                print("出错了？")
            return HtmlResponse(url=request.url, body=spider.broswer.page_source,
                                encoding="utf-8", request=request)
        if spider.name=='TmallInfo':
            try:
                spider.broswer.get(request.url)
            except TimeoutException as e:
                print("超时")
            return HtmlResponse(url=request.url,body=spider.broswer.page_source,
                                encoding="utf-8",request=request)
"""
            page = request.meta.get('page',1)
            try:
                spider.broswer.get(request.url)
                if page==1:
                    login=spider.wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static')))
                    login.click()
                    username = spider.wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, '#TPL_username_1')))
                    password = spider.wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, '#TPL_password_1')))
                    submit = spider.wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_SubmitStatic')))
                    username.clear()
                    password.clear()
                    username.send_keys('18801463693')
                    password.send_keys('lxh6338231')
                    time.sleep(2)
                    action = ActionChains(spider.browser)
                    frame = spider.wait.until(
                        EC.presence_of_element_located((By.ID,'_oid_ifr_')))
                    spider.browser.switch_to.frame(frame)
                    spider.browser.switch_to.default_content()
                    butt = spider.wait.until(
                        EC.presence_of_element_located((By.ID, 'nc_1_n1z')))
                    action.click_and_hold(butt).perform()
                    action.reset_actions()
                    action.move_by_offset(298, 0).perform()
                    submit.click()
                    cookies= spider.browser.get_cookies()
                    print(cookies)
                    print("登陆成功！！！！！！！！！！！！！！！！！！！！！！！！！！！")
                    print("！！！！！！！！！！！！！！！！！！！！！！！！！")
                    print("！！！！！！！！！！！！！！！！！！！！！！！！")
                    print("！！！！！！！！！！！！！！！！！！！！！！！")
                if page>1:
                    print(111111111111111111111111111111111111111111111111111111111111)
                    input = spider.wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
                    submit = spider.wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
                    print(222222222222222222222222222222222222222222222222222222222222)
                    input.clear()
                    input.send_keys(page)
                    submit.click()
                spider.wait.until(
                    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'),
                                                     str(page)))
                spider.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
                """



