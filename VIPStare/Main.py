#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 26/05/2018 00:04
# @Author  : DaBai
# @Site    : 
# @File    : Main.py
# @Software: PyCharm
import tkinter as tk
from VIPStare import Login as login

def ShowMainDialog():
    main_root = tk.Tk();
    w = main_root.winfo_screenwidth()
    h = main_root.winfo_screenheight()
    main_root.title("主界面")
    main_root.geometry("%dx%d" %(w, h))

    main_root.mainloop()