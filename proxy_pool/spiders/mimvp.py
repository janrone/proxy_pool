# -*- coding: utf-8 -*-
# import scrapy
# from proxy_pool.items import ProxyPoolItem

# class MimvpSpider(scrapy.Spider):
#     name = 'mimvp'
#     allowed_domains = ['mimvp.com']
#     start_urls = ['http://proxy.mimvp.com/free.php?proxy=in_tp',
#     'http://proxy.mimvp.com/free.php?proxy=in_hp',
#     'http://proxy.mimvp.com/free.php?proxy=out_tp',
#     'http://proxy.mimvp.com/free.php?proxy=out_hp']

#     def parse(self, response):
#         data = response.xpath('//table[@class="free-table table table-bordered table-striped"]/tbody/tr')
        
#             for x in data:
#                 item = ProxyPoolItem()
#                 info = x.xpath('td/text()').extract()
#                 print("info", info)
#                 item['ip'] = info[0].strip()
#                 item['protocol'] = info[3].strip()
#                 item['port'] = info[1].strip()
#                 item['types'] = info[2].strip()
#                 item['address'] = info[4].strip()
#                 item['website'] = 'mimvp.com'
#                 yield item
