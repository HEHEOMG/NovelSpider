# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from NovelSpider.items import NovelspiderItem


class NovelSpiderSpider(scrapy.Spider):
    name = 'novel_spider'
    allowed_domains = ['biquge.com.tw']
    # 待爬取小说目录页面链接，如：http://www.biquge.com.tw/18_18550/
    start_urls = ['http://www.biquge.com.tw/18_18550/']

    def parse(self, response):
        page = 0
        le = LinkExtractor(restrict_css='#list > dl:nth-child(1)')  # 创建提取规则
        links = le.extract_links(response)      # 提取链接
        if links:
            for link in links[0:3]:
                page += 1
                yield Request(link.url, callback=self.parseText, meta={'page': page})

    def parseText(self, response):
        capter = NovelspiderItem()
        capter['novelName'] = response.css('.bottem1 > a:nth-child(3)::text').extract_first()
        capter['nowPage'] = response.meta['page']
        capter['title'] = response.css('.bookname > h1:nth-child(1)::text').extract_first()
        capter['content'] = response.xpath('//*[@id="content"]').xpath('string(.)').extract_first()
        yield capter