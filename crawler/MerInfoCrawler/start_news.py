import os
import re
from crawler.MerInfoCrawler.Doc import Doc
urls = []
for url in open('href_cases.txt'):
    if re.match(r'.*?/.*?cn/.*?', url):
        os.system('scrapy crawl Huawei_next -a url='+url)
        Doc()