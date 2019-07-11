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
    except:
        return False


def scan(keywords):
    result = set()
    for page in range(0,30,10):
        # 只需要 5 页 的数据就够了
        url = 'https://www.baidu.com/s?wd={}&pn={}'.format(quote(keywords),page)
        try:
            headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'BAIDUID=832CF61CDAEF34C68E7CA06F591DF82A:FG=1; BIDUPSID=832CF61CDAEF34C68E7CA06F591DF82A; PSTM=1544962484; BD_UPN=12314753; BDUSS=RWclRJUURtR25qZWxKZWZiN0JuSlJVTWpKRjhvb3ROdmIyNnB0eEwwY2FVOWxjSVFBQUFBJCQAAAAAAAAAAAEAAADS9fNj0-~PxM600esAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABrGsVwaxrFcck; cflag=13%3A3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; delPer=0; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; H_PS_PSSID=1453_21088_20692_28774_28720_28558_28832_28584; B64_BOT=1; BD_CK_SAM=1; PSINO=1; sug=3; sugstore=1; ORIGIN=2; bdime=0; H_PS_645EC=87ecpN5CzJjR5UwprsIowJPhqh6m9t1xGvxRkjeNmvcXBhI86ytKIjXLMhQ',
            'Host': 'www.baidu.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

            }
            r = requests.get(url,headers=headers,timeout=20)
            soup = bs(r.content, 'lxml')
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
                with open('url_result.txt','a+',encoding='utf-8')as a:
                    a.write(ur + '\n')
                with open('url_log.txt','a+',encoding='utf-8')as a:
                    a.write(keywords + ':' + ur + '\n')

if __name__ == '__main__':
    inp = input('导入标题文本:')
    titles = list(set([x.strip() for x in open(inp,'r',encoding='utf-8').readlines()]))
    print('目标总数:{}'.format(len(titles)))
    with ThreadPoolExecutor(10) as p:
        # 开 10 个线程池
        res = [p.submit(scan,url) for url in titles]
