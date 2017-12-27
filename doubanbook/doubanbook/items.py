# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    writer=scrapy.Field()
    date=scrapy.Field()
    pagenum=scrapy.Field()
    ISBN=scrapy.Field()
    price=scrapy.Field()
    tags=scrapy.Field()
