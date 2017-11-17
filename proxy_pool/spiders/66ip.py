# -*- coding: utf-8 -*-
# __author__: vincentlc

import scrapy
from proxy_pool.items import ProxyPoolItem

class SixSixIpSpider(scrapy.Spider):
    name = '66ip'
    allowed_domains = ['66ip.cn']
    start_urls = []
    for i in range(1, 32):
        start_urls.append("http://www.66ip.cn/areaindex_"+str(i)+"/1.html")
        start_urls.append("http://www.66ip.cn/areaindex_"+str(i)+"/2.html")
        start_urls.append("http://www.66ip.cn/areaindex_"+str(i)+"/3.html")

    def parse(self, response):

        iplist = response.xpath('//*[@id="footer"]/div/table//tr')

        for x in iplist[1:-1]:
            ips = x.xpath('td[1]/text()').extract()[0]
            ports = x.xpath('td[2]/text()').extract()[0]
            types = x.xpath('td[3]/text()').extract()[0]
            protocols = x.xpath('td[4]/text()').extract()[0]

            yield ProxyPoolItem({
                'ip': ips,
                'protocol': protocols,
                'port': ports,
                'types': types
            })

