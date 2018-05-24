# NovelSpider
一个用来爬笔趣阁单本小说的爬虫


## 快速开始 :
1.在novel_spider 的start_urls中输入http://www.biquge.com.tw/网站中小说目录页面URL
2.若想直接生成TXT文件在settings文件中将ITEM_PIPELINES改为对于的pipelines,然后运行Begin.py,最后运行mergeNovel.py
  将下载的小说合成一本
3.若想存入数据库可直接将settings文件中将ITEM_PIPELINES改为对于的pipelines，然后在setting中配置mysql信息
