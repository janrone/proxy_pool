# -*- coding: utf-8 -*-
import scrapy
from proxy_pool.items import ProxyPoolItem

class A66ipSpider(scrapy.Spider):
    name = '66ip'
    allowed_domains = ['66ip.cn']
    start_urls = ['http://www.66ip.cn/']
    for i in range(2,10):
        url = 'http://www.66ip.cn/%d.html' % i
        start_urls.append(url)

    def parse(self, response):
        ip_list = response.xpath('//div[@class="containerbox boxindex"]//table//tr')[1:]
        ip = ip_list.xpath('./td/text()').extract()
        for i in range(0, len(ip), 5):
        #110.77.208.105	62225	泰国	高匿代理	2017年11月18日10时 验证
            print(ip[i], ip[i + 1], ip[i + 2], ip[i + 3], ip[i + 4])
            item = ProxyPoolItem()
            item['ip'] = ip[i].strip()
            item['port'] = ip[i + 1].strip()
            item['types'] = ip[i + 3].strip()
            item['address'] = ip[i + 2].strip()
            item['website'] = 'www.66ip.cn'
            yield item