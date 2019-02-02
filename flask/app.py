import flask
from flask import jsonify
import json
import urllib
from lxml import etree
import requests
from flask import request  #获取参数
# import json #post请求传入json对象时，通过json获取参数

def conn_mysql(sql):
    import pymysql
    conn = pymysql.connect(host='192.168.108.140', user='root', password='passwd', db='test', charset='utf8')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql)
    res = cur.fetchone()
    print(res)
    conn.commit()
    cur.close()
    conn.close()
    return res

server = flask.Flask(__name__) #创建一个flask对象
server.config['JSON_AS_ASCII'] = False

@server.route('/search', methods=['get','post'])
#根据名字获取电话号码
#http://127.0.0.1:8000/search?name=张艳红
def search():
    name = request.values.get('name') #获取参数
    # username = request.json.get('username') #入参为json类型时，必须用.json方式获取
    # password = request.json.get('password')
    if name:
        sql = 'select name,phnum from unis where name="%s"'%name
        data = conn_mysql(sql)
        if data is not None and data['name']== name:
            data['name']
            return jsonify(data)
        else:
            return '{"msg":"未找到该用户信息,请检查拼写是否有误!"}'
    else:
        return '{"msg":"请输入需要查找的用户名!"}'

		
		
def crawl_baike(keyword):
    dict1 = {}
    base_url = "https://baike.baidu.com/item/"
    url = base_url + keyword
    headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    try:
        html = requests.get(url, headers=headers,timeout=10).content.decode('utf-8')
        html = etree.HTML(html)
        description = html.xpath('//head/meta[@name="description"]/@content')
        dict1['searchUrl'] = url
        dict1['searchResult'] = description[0]
        return(dict1)
    except Exception as e:
        return None


@server.route('/baike', methods=['get','post'])	
#根据关键词搜索百度百科
#http://127.0.0.1:8000/baike?keyword=科比
def baike():
    keyword = request.values.get('keyword') #获取参数
    base_url = "https://baike.baidu.com/item/"
    url = base_url + keyword
    if keyword:
        data = crawl_baike(keyword)
        if data is not None:
            return jsonify(data)
            #return jsonify({'SearchResutdata': data})
            #return str(data)
        else:
            #return None
            return jsonify({'searchResult':"未找到匹配词条相关信息!",'searchUrl':url})
    else:
        return jsonify({'searchResult':"请重新输入其他搜索关键词!",'searchUrl':url})

server.run(port=8000,debug=True,host='0.0.0.0') #debug设置为True，修改接口信息后直接刷新接口即可；添加参数host='0.0.0.0'允许同一局域网内访问

