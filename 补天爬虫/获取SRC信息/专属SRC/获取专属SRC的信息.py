# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import requests

def parse_data(jsons):
    datas = (jsons['data'])
    real_data = (datas['list'])
    for d in real_data:
        print(d['host'])
        print(d['company_name'])
        # with open('srcname.txt','a+',encoding='utf-8')as a:
        #     a.write(d['host'].replace('www.','')+'\n')
        # print(d['company_name'])
        # with open('企业名称.txt','a+',encoding='utf-8')as a:
        #     a.write(d['company_name']+'\n')
url = 'https://www.butian.net/Reward/corps'
data = {
's': '3',
'p': '2',
'sort': '2'
}
r = requests.post(url=url, data=data)
parse_data(r.json())

# for d in real_data:
#     print(d['host'])
#     with open('srcname.txt','a+',encoding='utf-8')as a:
#         a.write(d['host'].replace('www.','')+'\n')
#     print(d['company_name'])
#     with open('企业名称.txt','a+',encoding='utf-8')as a:
#         a.write(d['company_name']+'\n')



