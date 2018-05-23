#!usr/bin/env python  
#-*- coding:utf-8 -*-  
# @Author:  呵呵 
# @File:    mergeNovel.py 
# @Time:    2018/04/{DAY} 
# @Software:PyCharm

import os


#获取目标文件夹的路径
path = os.path.dirname(__file__)
filedir = '%s/novel' % path
finalDir = '%s/novels' % path
if not os.path.exists(finalDir):
    os.makedirs(finalDir)
#获取当前文件夹中的文件名称列表
filenames = os.listdir(filedir)
print(filenames)
for filename in filenames:
    # 获取目录下小说章节列表
    capterNames = os.listdir(filedir+'/'+filename)
    # 打开指定目录下的文件，若没有则创建
    f = open(finalDir + '/' + filename+'.txt', 'a', encoding='utf-8')
    # 遍历章节名
    for pageNmae in range(len(capterNames)):
        print(pageNmae)
        filepath = filedir+'/' + filename + '/'+str(pageNmae+1) + '.txt'
        #遍历单个文件，读取行数
        for line in open(filepath, encoding='utf-8'):
            f.writelines(line)
        f.write('\n')
    #关闭文件
    f.close()

