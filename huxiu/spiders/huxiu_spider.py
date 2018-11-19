#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
from huxiu.items import HuxiuItem

import scrapy

class HuxiuSpider(scrapy.Spider):
    name = "huxiu"
    allowed_domains = ["huxiu.com"]

    def start_requests(self):
        start_urls = [
            "https://www.huxiu.com/"        
        ]

        for url in start_urls:
            yield scrapy.Request(url, 
                    headers = {
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9'
                    },
                callback = self.parse)
            
                
    def parse(self, response):
        for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            item = HuxiuItem()
            item['title'] = sel.xpath('h2/a/text()').extract()[0]
            item['link'] = sel.xpath('h2/a/@href').extract()[0]
            url = response.urljoin(item['link'])
            item['desc'] = sel.xpath('div[@class="mob-sub"]/text()').extract()[0]
            print('%s ||| %s ||| %s' % (item['title'],item['link'],item['desc']))

