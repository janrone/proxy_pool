# -*- coding: utf-8 -*-
import scrapy
import requests
import re
from proxy_pool.items import ProxyPoolItem


class NianshaoSpider(scrapy.Spider):
    name = 'nianshao'
    allowed_domains = ['nianshao.me']
    start_urls = []
    http_url = 'http://www.nianshao.me/?stype=1'
    https_url = 'http://www.nianshao.me/?stype=2'
    http_count = re.findall('</font>/(\d+)</strong>',requests.get(http_url).text)[0]
    #print(http_count)
    https_count = re.findall('</font>/(\d+)</strong>',requests.get(https_url).text)[0]
    #print(https_count)
    # start_urls = ['http://www.nianshao.me/?stype=1&page=1']
    for i in range(1,(int(http_count)+1)):
        start_urls.append('http://www.nianshao.me/?stype=1&page='+str(i))
    for i in range(1,(int(https_count)+1)):
            start_urls.append('http://www.nianshao.me/?stype=2&page='+str(i))

    def parse(self, response):
        ips = re.findall('<td style="WIDTH:110PX">(\d+\.\d+\.\d+\.\d+)</td>', response.text)
        ports = re.findall('<td style="WIDTH:40PX">(\d+)</td>', response.text)
        types = re.findall('<td style="WIDTH:135PX">([^<]+)</td>', response.text)
        protocols = re.findall('<td style="WIDTH:55PX">(HTTPS?)</td>', response.text)
        for ip, port, _type, protocol in zip(ips, ports, types, protocols):
            yield ProxyPoolItem({
                'ip': ip,
                'protocol': protocol,
                'port': port,
                'types': _type
            })
