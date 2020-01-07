# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SgeItem(scrapy.Item):
    source=scrapy.Field()
    date = scrapy.Field()
    Au95 =scrapy.Field()
    Au99 = scrapy.Field()
    Au100=scrapy.Field()
    iAu99 = scrapy.Field()
    AuTD = scrapy.Field()
    AuTN1 = scrapy.Field()
    AuTN2 = scrapy.Field()
    mAuTD = scrapy.Field()
    Pt95 = scrapy.Field()
    Ag99 = scrapy.Field()
    AgTD = scrapy.Field()
    PGC = scrapy.Field()

class SgeJrhqItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    Au95 =scrapy.Field()
    Au99 = scrapy.Field()
    Au100=scrapy.Field()
    iAu99 = scrapy.Field()
    AuTD = scrapy.Field()
    AuTN1 = scrapy.Field()
    AuTN2 = scrapy.Field()
    mAuTD = scrapy.Field()
    Pt95 = scrapy.Field()
    Ag99 = scrapy.Field()
    AgTD = scrapy.Field()
    PGC = scrapy.Field()
class JDItem(scrapy.Item):
    url = scrapy.Field()
    date = scrapy.Field()
    source=scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()
    shop=scrapy.Field()

class TaoBaoItem(scrapy.Item):
    url = scrapy.Field()
    date = scrapy.Field()
    source=scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()
    shop=scrapy.Field()

class TmallItem(scrapy.Item):
    url = scrapy.Field()
    date = scrapy.Field()
    source=scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()
    shop=scrapy.Field()

class JDInfoItem(scrapy.Item):
    date = scrapy.Field()
    info = scrapy.Field()
    shop = scrapy.Field()

class TmallInfoItem(scrapy.Item):
    date = scrapy.Field()
    info = scrapy.Field()
    shop = scrapy.Field()