# -*- coding: utf-8 -*-
import scrapy
import requests
import re
from proxy_pool.items import ProxyPoolItem


class NianshaoSpider(scrapy.Spider):
    name = 'nianshao'
    allowed_domains = ['nianshao.me']

    def start_requests(self):
        pages=[]
        
        for i in range(1,3):
            count = re.findall('</font>/(\d+)</strong>',requests.get('http://www.nianshao.me/?stype={protocol_id}'.format(protocol_id=i)).text)[0]
            for j in range(1,(int(count)+1)):
                url = 'http://www.nianshao.me/?stype={protocol_id}&page={page}'.format(protocol_id=i,page=j)
                page = scrapy.Request(url)
                pages.append(page)
        return pages

    def parse(self, response):
        ips = re.findall('<td style="WIDTH:110PX">(\d+\.\d+\.\d+\.\d+)</td>', response.text)
        ports = re.findall('<td style="WIDTH:40PX">(\d+)</td>', response.text)
        countrys = re.findall('<td style="WIDTH:135PX">([^<]+)</td>', response.text)
        protocols = re.findall('<td style="WIDTH:55PX">(HTTPS?)</td>', response.text)
        for ip, port, country, protocol in zip(ips, ports, countrys, protocols):
            yield ProxyPoolItem({
                'ip': ip,
                'protocol': protocol,
                'port': port,
                'country': country
            })
