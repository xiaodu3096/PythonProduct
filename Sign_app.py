#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 09/03/2018 23:32
# @Author  : DaBai
# @Site    : 
# @File    : Sign_app.py
# @Software: PyCharm

from tornado import web,ioloop,httpserver
import codecs
# 文件句柄
# 全局变量
Sign_File_Handle = open(r'sign.csv','a')
# 写表头
Sign_File_Handle.write('%s,%s,%s\n'% ('姓名','部门','工号'))


#逻辑处理模块
class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('Index.html')


#签到模块
class SignHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('Sign.html')


    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        number = self.get_argument('number')
        depart = self.get_argument('depart')
        # print(name,number,depart)
        # 收到数据
        # 处理，安全，过滤，检测
        # 写到文件
        Sign_File_Handle.write('%s,%s,%s\n'% (name,depart,number))
        Sign_File_Handle.flush()
        self.write('签到成功')



#路由
application = web.Application([
               (r'/index',MainPageHandler),
                (r'/sign',SignHandler)

        ])

#socket服务
if __name__ =='__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()