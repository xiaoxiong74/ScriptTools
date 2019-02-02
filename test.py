# -*- coding: utf-8 -*-
'''
@author: xiongyongfu
@contact: xyf_0704@sina.com
@file: test.py
@Software: PyCharm
@time: 2018/10/20 10:16
@desc:
'''

# import datetime
# today = datetime.date.today()
# print(today)
# t1=str(today)
# print(str(today))
# print(type(t1))
# tenmini = datetime.timedelta(days=1)
# tenmin_delay_today = today - tenmini
# print(tenmin_delay_today)
#
# fp = open("C:\\Users\\Administrator\\Desktop\\test.txt", 'w')
# fp.write('head')
# fp.write('\n')
# fp.write('content')
# fp.close()

# line='&nbsp;10月29日 14:43&nbsp;来自小米8周年旗舰手机'
# l1=line.split('&nbsp;')
# print(l1)
#
# import base64
#
# l2=['1.jpg','2.jpg','3.jpg']
# encodestr = list(map(lambda x:base64.b64encode(x.encode('utf-8')),l2))
# for i in encodestr:
#     print(str(i,'utf-8'))
# print(encodestr)


import csv
import sys

filename = sys.argv[1]
l = filename.split(".")
newfilename = l[0]+"new."+l[1]

# with open(filename,'r') as fp_in, open(newfilename,'w',newline='') as fp_out:
#     reader = csv.reader(fp_in)
#     next(fp_in, None)
#     writer = csv.writer(fp_out)
#     for row in reader:
#         tmp = []
#         for cell in row:
#             l1=cell.replace(",", "，").strip()
#             tmp.append(l1)
#         writer.writerow(tmp)

fp_in = open(filename,'r')
fp_out = open(newfilename,'w',newline='')
reader = csv.reader(fp_in)
next(fp_in, None)
writer = csv.writer(fp_out)
for row in reader:
    tmp = []
    for cell in row:
        l1=cell.replace(",", " ").replace("，", " ").strip()
        tmp.append(l1)
    writer.writerow(tmp)






















