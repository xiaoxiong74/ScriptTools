# *-* coding:utf-8 *-*
import requests
import time
import urllib
import pymongo
import datetime
import random
'''
获取重庆市区各楼盘房产销售信息(以网签登记为准)
url=http://www.cq315house.com/315web/HtmlPage/SpfQuery.htm#
'''
#############################浏览器列表#############################
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

#############################区域列表#############################
org_sites=["渝北","巴南","北碚","大渡口","江北","九龙坡","南岸","沙坪坝","渝中","两江新"]

#############################用途列表#############################
org_roomtypes=["住宅","办公","商铺"]

#############################url固定的部分#############################
url1='http://www.cq315house.com/315web/webservice/GetMyData999.ashx?projectname=&site=' #连接地区编码
url2='&kfs=&projectaddr=&pagesize=10&pageindex='                                        #连接页码
url3='&roomtype='                                                                       #连接房屋用途编码
url4='&buildarea='

#############################url地址格式#############################
# url='http://www.cq315house.com/315web/webservice/GetMyData999.ashx?projectname=&site=' \
#     '%25E4%25B9%259D%25E9%25BE%2599%25E5%259D%25A1' \                                 #地区编码格式
#     '&kfs=&projectaddr=&pagesize=10&pageindex=20&roomtype=' \                         #pageindex=20表示页码
#     '%25E4%25BD%258F%25E5%25AE%2585' \                                                #房屋用途编码格式
#     '&buildarea='
#需要两个条件 site  roomtype

#############################获取随机Header#############################
def get_randomHeader():
    header = {'User-Agent': random.choice(USER_AGENTS)}
    return header

#############################获取编码后的地区#############################
def get_sites():
    sites=[]
    for site in org_sites:
        code_site=urllib.parse.quote(urllib.parse.quote(site))                     #两次编码获得网址需要的地区编码格式
        sites.append(code_site)
        #urllib.parse.unquote(new)  #解码
        # params = urllib.parse.urlencode({'site': '渝北区', 'roomtype': '住宅' })   #可通过字典编码多个属性
        # print(params)
    return sites

#############################获取编码后的房屋用途#############################
def get_roomtypes():
    roomtypes=[]
    for roomtype in org_roomtypes:
        code_roomtype=urllib.parse.quote(urllib.parse.quote(roomtype))             #两次编码获得网址需要的房屋用途编码格式
        roomtypes.append(code_roomtype)
    return roomtypes



#############################拼接url地址#############################
def get_urls():
    urls=[]
    for roomtype in get_roomtypes():
        for site in get_sites():
            for i in range(1,31):                                                  #只循环40页即可完成一种类型所有数据
                tmp_list = []
                url=url1+str(site)+url2+str(i)+url3+str(roomtype)+url4
                tmp_list.append(url)
                tmp_list.append(urllib.parse.unquote(urllib.parse.unquote(site)))      #两次解码获得区域
                tmp_list.append(urllib.parse.unquote(urllib.parse.unquote(roomtype)))  #两次解码获得房屋类型
                urls.append(tmp_list)
    print(len(urls))
    return urls

#############################链接mongodb#############################
def connect_mongo():
    client = pymongo.MongoClient('192.168.110.51', 27017)            # 创建连接
    db = client['xiongyongfu']                                       # 连接的数据库
    collection = db['cq315_house_info']                              # 连接的表
    return collection

#############################获取昨天的日期#############################
def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday

#############################获取IP################################
def get_Ips():
    with open('C:\\Work\\pywork\\TestDemo\\proxies.txt', 'r') as f:
        ip_list1 = f.readlines()
        print("共有："+str(len(ip_list1))+"个可用IP")
        return ip_list1

#############################获取随机IP#############################
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append(ip.strip())
    proxy_ip = random.choice(proxy_list)
    proxies = {'https': proxy_ip}
    return proxies


def request_url(url,ip_list):
    proxies= get_random_ip(ip_list)
    headers = get_randomHeader()
    # print(proxies)
    html = requests.get(url, proxies=proxies, headers=headers, timeout=10)   #content.decode(encoding='utf-8')
    return html

#############################代理ip获取url内容#############################
# def get_house_content():
#     ip_list = get_Ips()
#     collection=connect_mongo()
#     result_count=0
#     print(getYesterday())
#     print("正在爬取房产信息...")
#     for url in get_urls():
#         #count=0
#         print(url[0],url[1],url[2])
#         response=request_url(url[0],ip_list)
#         # if response.status_code !=200 and count<3:
#         #     count+=1
#         #     print(response.status_code)
#         #     response = request_url(url, ip_list)
#         #     if response.status_code !=200:
#         #         continue
#         result=response.content.decode(encoding='utf-8')
#         if result:                   #过滤返回空列表的情况
#             print(result)
#             result={'ten_house_info':result,'updatetime':str(getYesterday())}
#             collection.insert(result)
#             result_count+=1
#         time.sleep(2)
#     print("爬取完毕,今日共爬取约："+str(result_count*10)+'条房产信息')

def get_house_content1():
    collection=connect_mongo()
    result_count=0
    headers = get_randomHeader()
    print(getYesterday())
    print("正在爬取房产信息...")
    for url in get_urls():
        #print(url[0], url[1], url[2])
        html = requests.get(url[0], headers=headers, timeout=10)
        result = html.content.decode(encoding='utf-8')
        if result:                   #过滤返回空列表的情况
            result={'site':url[1],'roomtype':url[2],'ten_house_info':result,'updatetime':str(getYesterday())}
            collection.insert(result)
            result_count+=1
            print(result)
        time.sleep(5)
    print("爬取完毕,今日共爬取约：" + str(result_count * 10) + '条房产信息')

if __name__ == '__main__':
    get_house_content1()
