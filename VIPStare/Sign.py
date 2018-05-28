#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 25/05/2018 23:26
# @Author  : DaBai
# @Site    : 
# @File    : Sign.py
# @Software: PyCharm

import sqlite3


conn = sqlite3.connect("vip.db");

c = conn.cursor();
c.execute('''CREATE TABLE Score (
           ID PRIMARY KEY NOT NULL,
           Name TEXT NOT NULL,
           Phone TEXT NOT NULL,
           CardID TEXT NOT NULL,
           CardScore TEXT NULL,
           Money TEXT NULL
         ); ''');

c.execute("INSERT INTO Score (ID,NAME,Phone,CardID,CardScore,Money) VALUES (1,'小杜1','18513335627', '123456789','1000', '10000')");


table = c.execute("SELECT * FROM Score")
for row in table:
    print("ID = ",row)


conn.commit();
conn.close();