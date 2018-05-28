#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 02/05/2018 20:25
# @Author  : DaBai
# @Site    : 
# @File    : Sign.py
# @Software: PyCharm


import requests
import re
import csv
import codecs


header={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    ,'Accept-Encoding': 'gzip, deflate'
    ,'Accept-Language': 'zh-CN,zh;q=0.9'
    ,'Connection': 'keep-alive'
    ,'Cookie': 'navCtgScroll=0; showNav=#nav-tab|0|0; _lxsdk_cuid=1630c555d232-0c3327a74df4b1-3a614f0b-1fa400-1630c555d24c8; _lxsdk=1630c555d232-0c3327a74df4b1-3a614f0b-1fa400-1630c555d24c8; __utma=1.1115006321.1524920311.1524920311.1524920311.1; __utmz=1.1524920311.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _hc.v="\"ca5587a4-30a5-41ce-b506-a20741e55bfb.1524920311\""; cy=2; cye=beijing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; s_ViewType=10; _lxsdk_s=1632141a4ee-a41-929-528%7C%7C76'
    ,'Host': 'www.dianping.com'
    ,'Upgrade-Insecure-Requests': '1'
    ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
def GetMessage(url,Page):
    DesCount = 0
    AvgCount = 0;
    data = []
    response = requests.get(url,headers = header)
    dianping_div1 = re.findall(r'<li class="" >(.*?)</li>',response.text,re.S)
    # print(dianping_div1)
    # f = codecs.open('大众点评.csv', 'a', 'utf_8_sig')
    # writer = csv.writer(f)
    if Page ==1:
        Type =  re.findall(r'<span itemprop="title">(.*?)</span>',response.text,re.S)
        if Type != []:
            print('美食类型：',Type[1].replace(' ', '').replace('\n', ''))
            # writer.writerow(['商铺名称', '商铺地址', '评论数', '人均'])
    for name in dianping_div1:
        names = re.findall(r'<h4>(.*?)</h4>',name,re.S)
        Address = re.findall(r'<span class="addr">(.*?)</span>',name,re.S)
        Des = re.findall(r'<b>(.*?)</b>\n条点评',name,re.S)
        Avgs = re.findall(r'人均\n                                        <b>(.*?)</b>',name,re.S)
        Urls = re.findall(r'href="(.*?)" data-click-name="shop_img_click" rel="nofollow" title=""  >',name,re.S)
        if Des == []:
            DesCount = 0
        else:
            DesCount = Des[0]

        if Avgs == []:
            AvgCount = '￥'+str(0)
        else:
            AvgCount = Avgs[0]
        # print([names[0],Address[0],DesCount,AvgCount,Urls[0]])
    print(GetDetailMessge(Urls))
    #     writer.writerow([names[0],Address[0],DesCount,AvgCount])
    # f.close()


def GetDetailMessge(url):
    Store_header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01'
        , 'Accept-Encoding': 'gzip, deflate'
        , 'Accept-Language': 'zh-CN,zh;q=0.9'
        , 'Connection': 'keep-alive'
        ,
        'Cookie': '_lxsdk_cuid=1630c555d232-0c3327a74df4b1-3a614f0b-1fa400-1630c555d24c8; _lxsdk=1630c555d232-0c3327a74df4b1-3a614f0b-1fa400-1630c555d24c8; __utma=1.1115006321.1524920311.1524920311.1524920311.1; __utmz=1.1524920311.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _hc.v="\"ca5587a4-30a5-41ce-b506-a20741e55bfb.1524920311\""; cy=2; cye=beijing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; s_ViewType=10; _lxsdk_s=16326ad2875-51f-2d5-877%7C%7C157'
        , 'Host': 'www.dianping.com'
        , 'Referer': 'http://www.dianping.com/shop/70783728'
        ,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        , 'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.get(url[0],headers = Store_header)
    Store_div1 = re.findall(r'<ul class="comment-list J-list" id="reviewlist-wrapper">(.*?)</ul>', response.text, re.S)

    return Store_div1[0]


for i in range(1,2):
    if i > 1:
        Page = 'p'+str(i)
    else:
        Page = ''
    url = "http://www.dianping.com/beijing/ch10/g117r2580"+Page
    GetMessage(url,i)