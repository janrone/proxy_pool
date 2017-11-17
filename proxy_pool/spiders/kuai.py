# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from proxy_pool.items import ProxyPoolItem

class KuaiSpider(scrapy.Spider):
    name = 'kuai'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/free/']

    def parse(self, response):
        iplist = response.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
        for x in iplist:
            data = x.xpath('td/text()').extract()
            item = ProxyPoolItem()
            item['ip'] = data[0]
            item['protocol'] = data[3]
            item['port'] = data[1]
            item['types'] = data[2]
            yield item
