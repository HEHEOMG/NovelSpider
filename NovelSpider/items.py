# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 小说名
    novelName = scrapy.Field()
    # 小说当前章节
    nowPage = scrapy.Field()
    # 小说当前章节名称
    title = scrapy.Field()
    # 小说章节内容
    content = scrapy.Field()
