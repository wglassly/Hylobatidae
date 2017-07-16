# -*- coding: utf-8 -*-
import scrapy


class AplusspiderSpider(scrapy.Spider):
    name = "APlusSpider"
    allowed_domains = ["http://www.a-hospital.com"]
    start_urls = ['http://http://www.a-hospital.com/w/百日咳']

    def parse(self, response):
        pass
