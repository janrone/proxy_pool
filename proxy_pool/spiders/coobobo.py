# -*- coding: utf-8 -*-
import scrapy


class CooboboSpider(scrapy.Spider):
    name = 'coobobo'
    allowed_domains = ['coobobo.com']
    start_urls = ['http://coobobo.com/']

    def parse(self, response):
        pass
