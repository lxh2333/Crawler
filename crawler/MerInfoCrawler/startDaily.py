from scrapy import cmdline
import datetime
import time
import shutil
import os
Record_Dir=r"crawls"
checkFile="Running.txt"
startTime=datetime.datetime.now()
mini_count=0
while True:
    IsRunning = os.path.isfile(checkFile)
    if not IsRunning:
        IsExsit = os.path.isdir(Record_Dir)
        if IsExsit:
            removeRec = shutil.rmtree(Record_Dir)
        time.sleep(5)
        os.system('scrapy crawl JD_css -s JOBDIR=crawls/store_JD_css')
        time.sleep(10)
        os.system('scrapy crawl JD_ctf -s JOBDIR=crawls/store_JD_ctf')
        time.sleep(10)
        os.system('scrapy crawl sge -s JOBDIR=crawls/store_sge')
        time.sleep(10)
        os.system('scrapy crawl tmall_css -s JOBDIR=crawls/store_tmall_css')
        time.sleep(10)
        os.system('scrapy crawl tmall_ctf -s JOBDIR=crawls/store_tmall_ctf')
        time.sleep(10)
        os.system('scrapy crawl JD_Info -s JOBDIR=crawls/store_JDInfo')
        time.sleep(10)
        os.system('scrapy crawl TmallInfo -s JOBDIR=crawls/store_TmallInfo')
        break
    time.sleep(1800)
    mini_count+=1
    if mini_count >=48:
        break