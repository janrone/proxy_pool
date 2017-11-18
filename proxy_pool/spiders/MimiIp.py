#!/usr/bin/env python
# __author__: vincentlc

import scrapy
from proxy_pool.items import ProxyPoolItem


class MimiipSpider(scrapy.Spider):
    name = "mimiip"
    allowed_domains = ["mimiip.com"]

    def start_requests(self):
        yield scrapy.Request("http://www.mimiip.com/gngao", callback=self.parse, meta={'level': 1})
        yield scrapy.Request("http://www.mimiip.com/gnpu", callback=self.parse, meta={'level': 1})
        yield scrapy.Request("http://www.mimiip.com/gntou", callback=self.parse, meta={'level': 1})
        yield scrapy.Request("http://www.mimiip.com/hw", callback=self.parse, meta={'level': 1})

    def parse(self, response):

        iplist = response.xpath('//table/tr')
        # next_page = response.xpath("//a[@class='next_page']/@href").extract_first()
        page_number = response.xpath("//div[@class='pagination']/a[last()-1]/text()").extract_first()
        level = response.meta['level']

        for x in iplist[1:-1]:
            ips = x.xpath('td[1]/text()').extract_first()
            ports = x.xpath('td[2]/text()').extract_first()
            protocols = x.xpath('td[5]/text()').extract_first()
            types = x.xpath('td[4]/text()').extract_first()

            yield ProxyPoolItem({
                'ip': ips,
                'protocol': protocols,
                'port': ports,
                'types': types
            })

        if level == 1 and page_number is not None:
            url = response.url
            for i in range(2, int(page_number) + 1):
                yield scrapy.Request("{0}/{1}".format(url, i), callback=self.parse, meta={'level': 2})
