# -*- coding: utf-8 -*-
'''
@author: xiongyongfu
@contact: xyf_0704@sina.com
@file: bendibao.py
@Software: PyCharm
@time: 2019/1/30 17:00
@desc: 爬取重庆市各地区派出地址、电话
'''

from lxml import etree
import requests
import pymysql

#写入mysql数据库
def insert_into_mysql(datas):
    conn = pymysql.connect(host='192.168.110.52', port=3306, user='root', passwd='passwd', db='xiongyongfu')
    cur = conn.cursor()
    for data in datas:
        insert_sql = "insert into cq_police_station(police_name,police_address,police_phone,police_work_time) values(%s,%s,%s,%s)"
        cur.execute(insert_sql, [data['网点名称'], data['地址'],data['电话'],data['上班时间']])
    conn.commit()
    cur.close()
    conn.close()
    print("Insert Data Done!")


def crawl(url):
    results = []
    html = requests.get(url, timeout=10).content.decode('utf-8')
    html = etree.HTML(html)
    base_info1 = html.xpath('//ul[@class="show"]')
    base_info2 = html.xpath('//ul[@class="hidden"]')
    base_info1.extend(base_info2)
    for item in base_info1:
        result = {}
        result['网点名称'] = item.xpath('./li[@class="li1"]/a/text()')[0]
        result['地址'] = item.xpath('./li[@class="li2"]/a/text()')[0]
        result['电话'] = item.xpath('./li[@class="li3"]/text()')
        if len(result['电话'])== 1:
            result['电话'] = result['电话'][0]
        else:
            result['电话'] = ''
        result['上班时间'] = item.xpath('./li[@class="li4"]/a/text()')
        if len(result['上班时间'])== 1:
            result['上班时间'] = result['上班时间'][0]
        else:
            result['上班时间'] = ''
        results.append(result)
    return results
    #print (results)

url = "http://cq.bendibao.com/cyfw/wangdian/2081.shtm"
datas =  crawl(url)
print(datas)
insert_into_mysql(datas)