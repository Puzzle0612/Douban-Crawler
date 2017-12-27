# -*- coding: utf-8 -*-
import scrapy
from doubanbook.items import DoubanbookItem

class DbbookSpider(scrapy.Spider):
    name = 'dbbook'
    #allowed_domains = ['https://book.douban.com/subject/27176647/']
    start_urls = ['https://book.douban.com/subject/27154489/']

    def parse(self, response):
        item=DoubanbookItem()
        selector = scrapy.Selector(response)
        item['name']="".join(selector.xpath("//*[@id=\"wrapper\"]/h1/span/text()").extract()).replace(' ','').replace('\n','')
        writer_case1="/".join(selector.xpath("//*[@id=\"info\"]/span[1]/a/text()").extract()).replace(' ','').replace('\n','')
        writer_case2="/""/".join(selector.xpath("//*[@id=\"info\"]/a[1]/text()").extract()).replace(' ','').replace('\n','')
        item['date']="".join(selector.xpath("//*[@id=\"info\"]/span[contains(./text(),'出版年')]/following::text()[1]").extract()).replace(' ','').replace('\n','')
        item['pagenum']="".join(selector.xpath("//*[@id=\"info\"]/span[contains(./text(),'页数')]/following::text()[1]").extract()).replace(' ','').replace('\n','')
        item['ISBN']="".join(selector.xpath("//*[@id=\"info\"]/span[contains(./text(),'ISBN')]/following::text()[1]").extract()).replace(' ','').replace('\n','')
        item['price']="".join(selector.xpath("//*[@id=\"info\"]/span[contains(./text(),'定价')]/following::text()[1]").extract()).replace(' ','').replace('\n','')
        item['tags']=";".join(selector.xpath("//*[@id=\"db-tags-section\"]/div/span/a/text()").extract()).replace(' ','').replace('\n','')
        if(writer_case1==''):
            item['writer']=writer_case2
        else:
            item['writer']=writer_case1
        yield item
        url_list = response.xpath("//div[@class='content clearfix']/dl/dd/a/@href").extract()
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse)


