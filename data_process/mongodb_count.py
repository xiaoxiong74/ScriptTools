# -*- coding: utf-8 -*-
'''
@author: xiongyongfu
@contact: xyf_0704@sina.com
@file: mongodb_count.py
@Software: PyCharm
@time: 2018/12/12 19:49
@desc:
'''

import pymongo
import pymysql

dict1={}
def connect_mongo(database):
    client = pymongo.MongoClient('192.168.110.51', 27017)     # 创建连接
    dict0={}
    #print(client.database_names())
    db = client[database]
    tables=db.collection_names()
    # 连接的数据库
    for table in tables:
        collection = db[table]
        dict_tmp={table:collection.count()}
        #print(dict_tmp)
        dict0.update(dict_tmp)
    return dict0
mongo_databases=['chenpeng', 'test', 'wanghaochen', 'shenli','weibotest', 'xuqiang', 'yangjie','xiongyongfu']
for database in mongo_databases:
    dicts = connect_mongo(database)
    #print(dicts)
    dict1.update(dicts)

#print (dict1)

def connect_mysql(database,table):
    db = pymysql.connect("192.168.110.52", "root", "passwd", database)
    cursor = db.cursor()
    sql="select count(*) from %s" %(table)
    cursor.execute(sql)
    result =cursor.fetchone()
    #print(table,result[0])
    db.close()
    return table,result[0]


mysql_dataases={'liangyuan_shenli':'jiaoyou_info','qqzone_shenli':'user_info','shenli_all':'qiyiwang'}
for key,value in mysql_dataases.items():
    table,count=connect_mysql(key,value)
    dict0={table:count}
    dict1.update(dict0)
for key,value in dict1.items():
    print(key,value)
#print(dict1)