# -*- coding: utf-8 -*-
import scrapy
from yongshi_scrapy.items import  YongshiScrapyItem

class YonshiSpider(scrapy.Spider):
    name = 'yongshi'
    allowed_domains = ['tieba.baidu.com']
    baseurl='http://tieba.baidu.com/f?kw=勇士&ie=utf-8&pn='
    offset = 0
    start_urls = [baseurl+str(offset)]



    def parse(self, response):
        print(response)
        item = YongshiScrapyItem()
        tieba_topics = response.xpath('//*[@id="thread_list"]/li[2]/div/div[2]/div[1]/div[1]/a')

        for tieba_topic in tieba_topics:
            item["tieba_topic"] = tieba_topic.extract()[0].encode('utf-8')
            yield item
        if self.offset < 118050:
            self.offset += 50
            url = self.baseurl + str(self.offset)
            scrapy.Request(url, callback=self.parse, dont_filter=True)




