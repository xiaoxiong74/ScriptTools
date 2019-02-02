# *-* coding:utf-8 *-*
from bs4 import BeautifulSoup
import lxml
import random
import json   
import requests
from lxml import etree
from bs4 import BeautifulSoup

s=requests.session()

headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Origin': 'https://ehire.51job.com',
    'Referer': 'https://ehire.51job.com/MainLogin.aspx',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Cookie': 'EhireGuid=04b6295d9bc9434fa7aaeb88af8dfa2a; RememberLoginInfo=member_name=5215542FA2FE9B7D6C611B66AB9BA5DD&user_name=D9AD803B6EA1BAF1; guid=9ee43e19d4fb11124e7027c49da0d0ce; slife=lowbrowser%3Dnot%26%7C%26; adv=adsnew%3D0%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttp%253A%252F%252Fwww.baidu.com%252Fs%253Fie%253Dutf-8%2526f%253D8%2526rsv_bp%253D1%2526tn%253D98564458_hao_pg%2526wd%253D51job%2526oq%253D51job%252525E6%2525258B%2525259B%252525E8%25252581%25252598%252525E7%252525BD%25252591%252525E7%252525AB%25252599%2526rsv_pq%253D941f9af60006856c%2526rsv_t%253D9ac6lkRMoh4RbHCgBayZuJK%25252FqJpmRD9ruoJgnTnCgVjmJpvXdV3D5klI2jFQND8Gbal8DX6p%2526rqlang%253Dcn%2526rsv_enter%253D1%2526inputT%253D225%2526rsv_sug3%253D76%2526rsv_sug1%253D28%2526rsv_sug7%253D100%2526rsv_sug2%253D0%2526rsv_sug4%253D721%2526rsv_sug%253D1%26%7C%26adsnum%3D2004282; LangType=Lang=&Flag=1; ASP.NET_SessionId=ccnqgt2ha5bjnhv4ojlbramn; HRUSERINFO=CtmID=257960&DBID=1&MType=06&HRUID=1964508&UserAUTHORITY=1000110010&IsCtmLevle=0&UserName=rdbjwx&IsStandard=1&LoginTime=09%2f30%2f2018+16%3a17%3a06&ExpireTime=09%2f30%2f2018+16%3a27%3a06&CtmAuthen=0000011000000001000111010000000011100011&BIsAgreed=true&IsResetPwd=0&CtmLiscense=10&AccessKey=10879709bdc5426f; AccessKey=1e8b8cc36fc8435',
}

login_url = 'https://ehire.51job.com/'
data ={
'__VIEWSTATE': '/wEPDwUKLTEzNTAwODM0MA9kFgICAQ9kFgICAQ8PFgIeCEltYWdlVXJsBUAvL2ltZzA3LjUxam9iY2RuLmNvbS9pbWVoaXJlL2VoaXJlMjAwNy9kZWZhdWx0bmV3L2ltYWdlL2xhbmcuZ2lmFgIeB09uQ2xpY2sFE3JldHVybiBTZXRMYW5nKCcnKTtkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQtja2JSZW1lbWJlcg==',
'hidRetUrl': '%2fNavigate.aspx%3fShowTips%3d11%26PwdComplexity%3dN',
'hidLangType': 'Lang=&Flag=1',
'hidAccessKey': '085bc91fa138469',
'fksc': 'a15d2efc1f7f4cde',
'hidEhireGuid': '04b6295d9bc9434fa7aaeb88af8dfa2a',
'hidTkey': '7be6cb92f03340d',
'hidVGuid': '609B270C2D985FDBA24B',
'txtMemberNameCN': '华为3Com',
'txtUserNameCN': 'rdbjwx',
'txtPasswordCN': 'h3c12345',
'ckbRemember': 'on',
'ctmName': '华为3Com',
'userName': 'rdbjwx',
'password': 'h3c12345',
'oldAccessKey': '085bc91fa138469',
'langtype': 'Lang=&Flag=1',
'isRememberMe': 'true',
'sc': 'a15d2efc1f7f4cde',
'ec': '04b6295d9bc9434fa7aaeb88af8dfa2a',
'returl': '%2fNavigate.aspx%3fShowTips%3d11%26PwdComplexity%3dN',
'referrurl': 'https://ehire.51job.com/MainLogin.aspx',
'tk': 'b2ab23436cb04f6',
'sk': '7be6cb92f03340d',
'verifyGuid': '609B270C2D985FDBA24B',
}

response = s.post(login_url, data=data,headers=headers)
print (response.status_code)
#print (response.content.decode("utf-8"))
url='https://ehire.51job.com/Candidate/ResumeView.aspx?hidUserID=94102923&hidEvents=23&pageCode=3&hidKey=4611a08babebadc28692e56070f72f8e'
r = s.get(url, headers=headers)
html=r.content.decode('utf-8')
#print(html)
html1 = etree.HTML(html)
element =html1.xpath('//table[@class="box1"]')
print(element)
for i in element:
    print(i)
#print (html)
# bs=BeautifulSoup(html,"html.parser")
# result=bs.select("td[class='plate1']")
# #esult=bs.select('td.plate1')
# #print (len(result),result[0].get_text())
# print('***************************************基本信息************************************************************')
# base_info=bs.select('table.box1')
# #print(bs.select('table.box1'))
# base1=bs.find('table',class_='box1')
# print(base1.)
# #base_info=BeautifulSoup(base_info,"html.parser")
# #name=base_info.findAll('tr')
# print('***************************************最近工作************************************************************')
# recent_work=bs.select('table.box2')
# print(bs.select('table.box2'))
# print('******************************************其他*************************************************************')
# other_info=bs.select('table.box')
# print(bs.select('table.box'))


#print(r.content.decode('utf-8'))