from scrapy import cmdline
from ProxyPool.schedule import Schedule
import os,sys,time

s=Schedule()
s.run()

os.system('scrapy crawl JD_css -s JOBDIR=crawls/store_JD_css')
time.sleep(5)
os.system('scrapy crawl JD_ctf -s JOBDIR=crawls/store_JD_ctf')
time.sleep(5)
os.system('scrapy crawl sge -s JOBDIR=crawls/store_sge')
time.sleep(5)
os.system('scrapy crawl tmall_css -s JOBDIR=crawls/store_tmall_css')
time.sleep(5)
os.system('scrapy crawl tmall_ctf -s JOBDIR=crawls/store_tmall_ctf')
time.sleep(5)
os.system('scrapy crawl JD_Info -s JOBDIR=crawls/store_JDInfo')
time.sleep(5)
os.system('scrapy crawl TmallInfo -s JOBDIR=crawls/store_TmallInfo')
