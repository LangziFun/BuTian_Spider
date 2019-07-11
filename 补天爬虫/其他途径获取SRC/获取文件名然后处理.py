# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun

import os
import re


all_lists = []

for a,b,c in os.walk('.'):
    for i in c:
        path = os.path.join(a,i)
        if '.txt' in path:
            all_lists.append(path)
print(all_lists)


all_urls = set()

for i in all_lists:
    print('*'*50)
    try:
        urls = [x for x in open(i,'r',encoding='utf-8').readlines()]
        for i in urls[1:]:
            try:
                domain = i.split('	')[0]
                print('域名:' + domain)
                all_urls.add(domain.strip())
            except:
                pass
    except Exception as e:
        print(e)

    try:
        urls = [x for x in open(i,'r',encoding='gbk').readlines()]
        for i in urls[1:]:
            try:
                domain= i.split('	')[0]
                print('域名:' + domain)
                all_urls.add(domain.strip())
            except:
                pass
    except Exception as e:
        print(e)
    print('*'*50)

print(len(all_urls))

with open('所有的src地址.txt','a+',encoding='utf-8')as a:
    for i in all_urls:
        if '.edu.' not in i and '.gov.' not in i:
            a.write(i + '\n')