#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 28/03/2018 20:38
# @Author  : DaBai
# @Site    : 
# @File    : Sign.py
# @Software: PyCharm


from tornado import web,ioloop,httpserver
from create_sign_code import get_code_by_str

class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('index.html')

class CodeHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        code_img_handler = get_code_by_str('http:127.0.0.1:8080/sign')
        self.write(code_img_handler.getvalue())

class SignHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('Sign.html')

application = web.Application([
        (r"/login",MainPageHandler),
        (r"/sign",SignHandler),
        (r"/code",CodeHandler)
        ])

if __name__ =='__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()