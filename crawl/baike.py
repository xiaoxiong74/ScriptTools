# -*- coding: utf-8 -*-
'''
@author: xiongyongfu
@contact: xyf_0704@sina.com
@file: baike.py
@Software: PyCharm
@time: 2019/1/25 10:40
@desc:
'''
import requests
import time
import urllib
from lxml import etree
import re

base_url = "https://baike.baidu.com/item/"
key_words = "杜兰特"
url = base_url + key_words
headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
html = requests.get(url, headers=headers,timeout=10).content.decode('utf-8')
#print(html)
dict1 = {}
html = etree.HTML(html)
description = html.xpath('//head/meta[@name="description"]/@content')
dict1['url'] = url
dict1['description'] = description
print(dict1)