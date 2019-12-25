# -*- coding: utf-8 -*-
import scrapy
from xiachufang.items import XiachufangItem


class XcfCatsSpider(scrapy.Spider):
    name = 'xcf'
    allowed_domains = ['www.xiachufang.com']
    start_urls = ['http://www.xiachufang.com/category/']

    def parse(self, response):
        links = response.xpath('//li/a[@target="_blank"]/@href').extract()
        for link in links:
            category_url = response.urljoin(link)
            yield scrapy.Request(url=category_url, callback=self.parse_recipe_url)

    def parse_recipe_url(self, response):
        if response.status == 429:
            self.crawler.engine.close()
        links = response.xpath('//ul[@class="list"]/li/div/a/@href').extract()
        for link in links:
            recipe_url = response.urljoin(link)
            yield scrapy.Request(url=recipe_url, callback=self.parse_recipe_detail)

    def parse_recipe_detail(self, response):
        item = XiachufangItem()
        item['name'] = response.xpath('//h1[@class="page-title"]/text()').extract_first().strip()
        item['category'] = response.xpath('//div[@class="page-container"]/ol/li[2]/a/@title').extract_first()
        item['recipe_url'] = response.url
        item['cover_image_url'] = response.xpath('//div[@class="block recipe-show"]/div[1]/img/@src').extract_first()
        if response.xpath('//div[@class="score float-left"]'):
            item['score'] = response.xpath('//div[@class="score float-left"]/span/text()').extract_first()
        else:
            item['score'] = None
        item['cooked_num'] = response.xpath('//div[@class="cooked float-left"]/span/text()').extract_first()
        item['author'] = response.xpath('//div[@class="author"]/a/span/text()').extract_first()
        if response.xpath('//div[@itemprop="description"]'):
            item['description'] = ''.join(response.xpath('//div[@itemprop="description"]/text()').extract()).strip()
        else:
            item['description'] = ''
        item['ingredient'] = [i.strip() for i in response.xpath('//tr[@itemprop="recipeIngredient"]/td[1]//text()').extract() if i.strip() != '']
        item['steps'] = response.xpath('//div[@class="steps"]/ol/li/p/text()').extract()
        item['create_time'] = response.xpath('//span[@itemprop="datePublished"]/text()').extract_first()
        item['collection'] = response.xpath('//div[@class="pv"]/text()').extract_first().split()[0]

        return item