# -*- coding: utf-8 -*-
'''
@author: xiongyongfu
@contact: xyf_0704@sina.com
@file: sensitive_word.py
@Software: PyCharm
@time: 2018/11/13 16:33
@desc:
'''

import os
import xlrd
import pandas


readbook = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\WORK\爬虫\重庆公交分析\敏感词库\minganciku_Jisuxz.com\mgck2017\敏感词库表统计.xlsx')
sheet = readbook.sheet_by_name('Sheet1')
nrows = sheet.nrows#行
ncols = sheet.ncols#列



with open(r'C:\Users\Administrator\Desktop\WORK\爬虫\重庆公交分析\敏感词库\sensitive.txt','w')  as f:
    for i in range(1,nrows):
        f.write(str(sheet.cell(i,1).value) + '\t' + str(sheet.cell(i,3).value) + '\n')


readbook1 = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\WORK\爬虫\重庆公交分析\敏感词库\涉政关键词\涉政关键词（4至8日）.xls')
sheet1 = readbook1.sheet_by_name('Sheet1')
nrows1 = sheet1.nrows#行
ncols1 = sheet1.ncols#列

with open(r'C:\Users\Administrator\Desktop\WORK\爬虫\重庆公交分析\敏感词库\sensitive.txt','a') as f:
    for i in range(1,nrows1):
        l1=[]
        l1.extend(str(sheet1.cell(i,0).value).split(" "))
        for word in l1:
            if word:
                f.write('政治' + '\t' + word + '\n')


##敏感词去重




