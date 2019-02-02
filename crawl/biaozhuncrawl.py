# -*- coding: utf-8 -*-
'''
@author: xiongyongfu
@contact: xyf_0704@sina.com
@file: biaozhuncrawl.py
@Software: PyCharm
@time: 2018/12/8 14:29
@desc:
'''
import requests
import time
import urllib
from lxml import etree
import re
import pymysql

with open('C:\\Users\\Administrator\\Desktop\\biaozhuntest.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        data = line.split('\t')
        print(data[0],data[1],data[2])
        page_list = []
        third1_html = requests.get(str(data[2].strip()), timeout=10).content.decode('utf-8')
        #print(third1_html)
        third1_html = etree.HTML(third1_html)
        page_text = third1_html.xpath('//span[contains(@title,"页")]/text()')
        pages = re.findall(r'\d+',str(page_text))
        if len(len[pages]==0):
            page_list.append[data[2]]
        elif int(pages[0]) >= 2:
            for page in range(int(pages[0])):
                page_list.append(data[2][0:-6]+str(page+1)+'.html')
        else:
            page_list.append[data[2]]
        #print(page_list)
        time.sleep(5)
        #db = pymysql.connect("192.168.110.52", "root", "passwd", "xiongyongfu")
        for page in page_list:
            third_html = requests.get(page, timeout=10).content.decode('utf-8')
            third_html = etree.HTML(third_html)
            third_desc = third_html.xpath('//a[@class="s xst"]/text()')
            with open("C:\\Users\\Administrator\\Desktop\\biaozhun1.txt", 'a+') as f:
                for l in third_desc:
                    if '发帖管理' in l or '金币活动' in l or '反馈专贴' in l or '网新手指引' in l:
                        continue
                    else:
                        results = str(data[0])+'\t'+str(data[1])+'\t'+str(l)+'\n'
                        print(results)
                        try:
                            f.write(results)
                        except (UnicodeEncodeError,IndexError) as e:
                            print(e)