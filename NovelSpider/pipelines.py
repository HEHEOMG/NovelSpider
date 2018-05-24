# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from twisted.enterprise import adbapi

"""
这个类将抓取到的小说按章节放入文件夹中
"""
class NovelspiderPipeline(object):

    def open_spider(self,spider):
        """
        获取当前文件上一级目录地址
        """
        self.path = os.path.dirname(os.path.dirname(__file__))


    def process_item(self, item, spider):
        """
        将各章节放入文件夹中
        """
        dirPath = '%s/novel/%s' % (self.path, item['novelName'])
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        fiename = dirPath +'/'+str(item['nowPage'])+'.txt'
        with open(fiename, 'a', encoding='utf-8') as f:
            f.write(item['title'] + '\n')
            f.write(item['content'] + '\n')
        f.close()
        return item

class MySQLPipeline(object):

    def open_spider(self, spider):
        db = spider.settings.get("MYSQL_DB_NAME", "scrapy_default")
        host = spider.settings.get('MYSQL_HOST', "localhost")
        port = spider.settings.get("MYSQL_PORT", 3306)
        user = spider.settings.get('MYSQL_USER', "root")
        passwd = spider.settings.get("MYSQL_PASSWORD", "root")

        # 连接mysql数据库，创建游标
        self.dbpool = adbapi.ConnectionPool('pymysql', host=host, db=db, port=port, user=user,
                                            password=passwd, charset="utf8")

    def close_spider(self, spider):
        """
        该方法用于数据库插入完成后插入数据
        """
        self.dbpool.close()

    def process_item(self, item, spider):
        """
        向数据库插入数据
        """
        self.dbpool.runInteraction(self.insert_db, item)

        return item

    def insert_db(self, tx, item):
        """
        sql语句构造方法
        """
        values = (item["novelName"],
                  item["nowPage"],
                  item["title"],
                  item["content"],
        )

        sql = "INSERT INTO novels(novelName, nowPage, title, content) VALUES(%s, %s, %s, %s)"
        tx.execute(sql, values)




