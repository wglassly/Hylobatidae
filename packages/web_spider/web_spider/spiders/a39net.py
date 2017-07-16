# -*- coding: utf-8 -*-
import scrapy


class A39netSpider(scrapy.Spider):
    name = "39net"
    allowed_domains = ["http://jbk.39.net/"]
    start_urls = ['http://jbk.39.net/bw']




    def parse(self, response):

        def find_urls(response):
            next_path = response.xpath('//*[@id="res_tab_1"]/div[11]/a[12]/@href').extract()
            print("result :" + next_path[0])
            for sel in response.xpath('//*[@id="res_tab_1"]/div'):
                url = sel.xpath("dl/dt/h3/a/@href").extract()
                utype = sel.xpath("dl/dt/span[2]/text()").extract()

                yield( { "url": url, "utype":utype })

            yield( scrapy.http.Request(next_page(response), callback=find_urls))

        for url in find_urls(response):
            print(url)
            yield ( scrapy.http.Request(url['url'][0] +'jbzs', callback = self.parser_detail))


    def parser_detail(self, response):

            item = {}
            title_name = response.xpath("/html/body/section/div[1]/span/b").extract()
            introduct = response.xpath ("/html/body/section/div[3]/div[1]/div[1]/dl[1]/dd/text()").extract()
            item['name'] = title_name
            item["introduct"] = introduct
            item['type'] = url['utype'][0]
            sel = response.xpath("/html/body/section/div[3]/div[1]/div[1]")
            if sel:
                for data in sel.xpath("/dl"):
                    for item in data.xpath("/dd"):
                        key = data.xpath('/i').extract().replace("：",'')
                        value = data.xpath("/a/text()").extract()
                        item[key] =value
            yield(item)
