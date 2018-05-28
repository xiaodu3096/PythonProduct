#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 25/05/2018 21:34
# @Author  : DaBai
# @Site    : 
# @File    : Login.py
# @Software: PyCharm
import  sqlite3
from tkinter import *
from VIPStare import CreateUser as cu
from VIPStare import Main as mainDialog

def GetMessage():
    tab = cu.GetUser(0)
    if(tab!=""):
        mainDialog.ShowMainDialog()
        CloseTk(root)
    else:
        print(123)

def ShowTK(root):
    #标题
    root.title("VIPStare")
    #窗口大小 窗口位置
    root.geometry("400x150+800+300")
    #标签控件
    label = Label(root,text="账号：",font=('微软雅黑',16),fg='#000000')
    label.grid(row = 0,column = 0)

    #输入框
    entry = Entry(root,font=('微软雅黑',20))
    entry.grid(row = 0,column = 1)
    #标签控件
    label_UserName = Label(root,text="密码：",font=('微软雅黑',16),fg='#000000')
    label_UserName.grid(row = 1,column = 0)

    #输入框
    entry_Pass = Entry(root,text="123",font=('微软雅黑',20))
    entry_Pass.grid(row = 1,column = 1)
    #登录按钮
    button_Sign = Button(root,text='登录',font=('微软雅黑',16),width = 10,command = GetMessage)
    button_Sign.grid(row = 2,column = 1)

    #显示窗口 消息循环
    root.mainloop()

def CloseTk(root):
    root.mainloop(1)

if __name__ == '__main__':
    # 创建窗口
    root = Tk();
    ShowTK(root)