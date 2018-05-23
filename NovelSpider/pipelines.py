# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class NovelspiderPipeline(object):

    def open_spider(self,spider):
        self.path = os.path.dirname(os.path.dirname(__file__))
        print(self.path)

    def process_item(self, item, spider):
        dirPath = '%s/novel/%s' % (self.path, item['novelName'])
        print(dirPath)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        fiename = dirPath +'/'+str(item['nowPage'])+'.txt'
        with open(fiename, 'a', encoding='utf-8') as f:
            f.write(item['title'] + '\n')
            f.write(item['content'] + '\n')
        f.close()
        return item
