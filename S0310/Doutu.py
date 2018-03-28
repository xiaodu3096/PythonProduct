#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/03/2018 20:41
# @Author  : DaBai
# @Site    : 
# @File    : Doutu.py
# @Software: PyCharm

import requests
import re
import pymysql


db = pymysql.connect(host='127.0.0.1',port=3306,db='db',user='root',passwd='root',charset='utf-8')

# cursor = db.cursor()
# cursor.execute('select * from images')



def getImageList(page = 1):
   html = requests.get('http://www.doutula.com/article/list/?page=%s'% page).text
   reg = r'data-original="(.*?)".*?alt="(.*?)"'
   # print(html.text)
   # 增加效率
   # S 多行匹配
   reg = re.compile(reg,re.S)
   imagesList = re.findall(reg,html)
   print(imagesList)
   for i in imagesList:
      pass




getImageList()

