#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 25/05/2018 23:32
# @Author  : DaBai
# @Site    : 
# @File    : CreateUser.py
# @Software: PyCharm
import sqlite3

conn = sqlite3.connect("vip.db");

c = conn.cursor();


#创建表
def CreateDataBase():
    c.execute('''CREATE TABLE Score (
            ID INTEGER PRIMARY KEY NOT NULL,
            Name TEXT NOT NULL,
            Phone TEXT NOT NULL,
            CardID TEXT NOT NULL,
            CardScore DOUBLE NULL DEFAULT 0,
            Money DOUBLE NULL DEFAULT 0
          ); ''');

#创建用户
def CreateUser(Name,Phone,CardID,CardScore,Money):
    conn = sqlite3.connect("vip.db");

    c = conn.cursor();
    # c.execute("INSERT INTO Score (NAME,Phone,CardID,CardScore,Money) VALUES (?,?,?,?,?)",Name,Phone,CardID,CardScore,Money);
    c.execute("INSERT INTO Score (NAME,Phone,CardID,CardScore,Money) VALUES (?,?,?,?,?)", '小杜1', '18513335627', '123456789',
              1000, 10000);
    conn.commit();
    conn.close();

# 获取用户信息
def GetUser(CardID):
    if(CardID > 0):
        conn = sqlite3.connect("vip.db");
        c = conn.cursor();
        Table = c.execute("SELECT * FROM Score WHERE ID = 1");
        rows = c.fetchall()
        conn.close();
        return rows;
    else:
        print('123123123')


