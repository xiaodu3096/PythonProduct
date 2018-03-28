#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 28/03/2018 20:20
# @Author  : DaBai
# @Site    : 
# @File    : create_sign_code.py
# @Software: PyCharm
import qrcode
import io

def get_code_by_str(text):
    if not isinstance(text,str):
        print("请输入字符串参数")
        return None
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image()
    img_data = io.BytesIO()
    img.save(img_data)
    return img_data
    # print(img_data.getvalue())


# get_code_by_str("http://www.baidu.com")