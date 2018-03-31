#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 30/03/2018 21:40
# @Author  : DaBai
# @Site    : 
# @File    : Thred.py
# @Software: PyCharm

import threading
import time

# def Hi(num):
#     print("hello %s",num)
#     time.sleep(3)
#
#
# if  __name__=='__main__':
#     t1 = threading.Thread(target=Hi,args=(10,))
#     t1.start()
#
#     t2 = threading.Thread(target=Hi,args=(9,))
#     t2.start()
#     print("endof")
#同时打印出上述3行数据，并且3秒后结束


def music():
    print("begin to listen %s",time.ctime())
    time.sleep(3)
    print("end to listen %s",time.ctime())


def game():
    print("begin to game %s", time.ctime())
    time.sleep(5)
    print("end to game %s", time.ctime())


if __name__ =='__main__':
    t1 = threading.Thread(target=music)
    t2 = threading.Thread(target=game)
    t1.start()
    t2.start()
    t1.join()
    # t2.join()
    print("ending...")

