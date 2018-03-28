#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 14/03/2018 21:12
# @Author  : DaBai
# @Site    : 
# @File    : index.py
# @Software: PyCharm

from flask import  Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
