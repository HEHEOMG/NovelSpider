#!usr/bin/env python  
#-*- coding:utf-8 -*-  
# @Author:  呵呵 
# @File:    Begin.py 
# @Time:    2018/04/{DAY} 
# @Software:PyCharm

from scrapy import cmdline

cmdline.execute(['scrapy', 'crawl', 'novel_spider'])