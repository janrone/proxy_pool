# -*- coding: utf-8 -*-
import scrapy
import re
from proxy_pool.items import ProxyPoolItem

class NianshaoSpider(scrapy.Spider):
    name = 'nianshao'
    allowed_domains = ['nianshao.me']

    def start_requests(self):
        for i in range(1,3):
            for j in range(1,161):
                url = 'http://www.nianshao.me/?stype={protocol_id}&page={page}'.format(protocol_id=i,page=j)
                yield scrapy.Request(url)

    def parse(self, response):
        ips = re.findall('<td style="WIDTH:110PX">(\d+\.\d+\.\d+\.\d+)</td>', response.text)
        ports = re.findall('<td style="WIDTH:40PX">(\d+)</td>', response.text)
        addresses = re.findall('<td style="WIDTH:135PX">([^<]+)</td>', response.text)
        protocols = re.findall('<td style="WIDTH:55PX">(HTTPS?)</td>', response.text)
        for ip, port, address, protocol in zip(ips, ports, addresses, protocols):
            yield ProxyPoolItem({
                'ip': ip,
                'protocol': protocol,
                'port': port,
                'address': address,
                'website': 'www.nianshao.me'
            })
