# -*- coding:utf-8 -*-
import requests
from concurrent.futures import ThreadPoolExecutor
import time
import random
def run(url):
    try:
        time.sleep(random.randint(1,3))
        r = requests.get(url,timeout=5)
        data = (r.json()['data']['list'])
        print('当前爬行到第{}页  数量: {}'.format(url.replace('https://www.butian.net/Loo/index/p/', ''),len(data)))

        for i in data:
            #print(i['title'].replace('发现了','').split('的')[0])
            # 下面两行是保存数据
            with open('厂商.txt','a+',encoding='utf-8')as a:
                a.write(str(i['title'].replace('发现了','').split('的')[0])+ '\n')
    except Exception as e:
        print(e)
        run(url)
if __name__ == '__main__':
    tasks = ['https://www.butian.net/Loo/index/p/{}'.format(id) for id in range(1,6293)]
    with ThreadPoolExecutor(10) as p:
        res= [p.submit(run,url) for url in tasks]