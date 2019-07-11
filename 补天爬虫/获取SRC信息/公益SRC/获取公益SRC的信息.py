# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import requests
import re
import time
headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection': 'keep-alive',
'Content-Length': '16',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie':'改成你自己的',
'Host': 'www.butian.net',
'Origin': 'https://www.butian.net',
'Referer': 'https://www.butian.net/Reward/plan',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'

}
def parse_data(jsons):
    datas = (jsons['data'])
    real_data = (datas['list'])
    for d in real_data:
        print(d['company_name'])
        # with open('企业名称.txt','a+',encoding='utf-8')as a:
        #     a.write(d['company_name']+'\n')

for i in range(1,175):
    print('目前获取第 {} 页'.format(i))
    url = 'https://www.butian.net/Reward/pub'
    data = {
        's': '1',
        'p': i
    }
    r = requests.post(url=url, data=data)
    try:
        parse_data(r.json())
    except Exception as e:
        print(e)

# for d in real_data:
#     print(d['host'])
#     with open('srcname.txt','a+',encoding='utf-8')as a:
#         a.write(d['host'].replace('www.','')+'\n')
#     print(d['company_name'])
#     with open('企业名称.txt','a+',encoding='utf-8')as a:
#         a.write(d['company_name']+'\n')



