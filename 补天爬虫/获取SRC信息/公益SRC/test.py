# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import requests
import re
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

import requests


def parse_data(jsons):
    datas = (jsons['data'])
    real_data = (datas['list'])
    for d in real_data:
        print(d['company_name'])


url = 'https://www.butian.net/Reward/pub'
data = {
    's': '1',
    'p': '1'
}
r = requests.post(url=url, data=data)
parse_data(r.json())



