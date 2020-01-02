# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import requests
import re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote,urlparse
from bs4 import BeautifulSoup as bs
from requests.packages import urllib3
urllib3.disable_warnings()
import random,time
import datetime,os

filenames = (str(datetime.datetime.now()).replace(' ','-').replace(':','-').split('.')[0])

servers = ['220.181.112.244','123.125.114.144','180.97.33.107','180.97.33.108','61.135.169.121','14.215.177.38','183.232.231.172','61.135.169.125']

def Get_Resp(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    try:
        r = requests.get(url,timeout=10,headers=headers,verify=False)
        if '没有找到与' in r.content.decode() and '相关的网页'in r.content.decode():
            # print(r.content.decode())
            # print('当前网站无信息:{}'.format(url))
            return False
        return r.content
    except Exception as e:
        # print(e)
        baidu_url = url.split('//')[1].split('/')[0]
        baidu_server = random.choice(servers)
        url = url.replace(baidu_url,baidu_server)
        print('替换地址百度源IP : '+str(baidu_server))
        return Get_Resp(url)
        #return None


def Check_Keyword(url,keyword):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    try:
        r = requests.get(url,headers=headers,timeout=20,verify=False)
        encoding = requests.utils.get_encodings_from_content(r.text)[0]
        content = r.content.decode(encoding,'replace')
        if keyword in content:
            return True
        else:
            return False
    except Exception as e:
        return False

def scan(keywords):
    result = set()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    for page in range(0,500,10):
        # 只需要 50 页 的数据就够了
        url = 'https://www.baidu.com/s?wd={}&pn={}'.format(quote(keywords),page)
        try:
            r = Get_Resp(url)
            if r == False:
                break
            soup = bs(r, 'lxml')
            # 如果报错，就把上面这行 改成 soup = bs(r.content, 'html.parse')
            urls = soup.find_all(name='a', attrs={'data-click': re.compile(('.')), 'class': None})
            for url_ in urls:
                r_ = requests.get(url=url_['href'], headers=headers, timeout=20)
                if r_.status_code == 200 or r_.status_code == 302:
                    u = urlparse(r_.url)
                    ur = u.scheme+'://'+u.netloc
                    result.add(ur)
        except Exception as e:
            pass
    if result != {}:
        for ur in result:
            res = Check_Keyword(ur, keywords)
            if res == True:
                print('当前关键词获取成功:{} 对应网址: {} '.format(keywords, ur))
                with open(filenames+'/'+'url_result.txt','a+',encoding='utf-8')as a:
                    a.write(ur + '\n')
                with open(filenames+'/'+'url_log.txt','a+',encoding='utf-8')as a:
                    a.write(keywords + '-->' + ur + '\n')

if __name__ == '__main__':
    if os.path.exists(filenames):
        pass
    else:
        os.mkdir(filenames)
    print('''

             _                           _
            | |                         (_)
            | |     __ _ _ __   __ _ _____
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      
                               |___/       

    ''')
    time.sleep(5)
    inp = input('导入关键词文本:')
    titles = list(set([x.strip() for x in open(inp,'r',encoding='utf-8').readlines()]))
    print('导入文本目标总数:{}'.format(len(titles)))
    with ThreadPoolExecutor() as p:
        # 开 10 个线程池
        res = [p.submit(scan,url) for url in titles]
