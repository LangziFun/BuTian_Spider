# -*- coding:utf-8 -*-
import requests
import re
import random
import datetime
import time
from pyecharts import WordCloud,Bar
from collections import Counter
import jieba.analyse
import copy

def run_wordcloud(name,value,types):
    wordcloud = WordCloud(title=types,width=1500,height=1000)
    wordcloud.add("", name, value, word_size_range=[20, 100])
    wordcloud.render(types+'.html')

def run_bar(name,value,types):
    bar = Bar(title=types)
    bar.use_theme('light')
    bar.add('漏洞数量', name, value, is_more_utils=True)
    # 添加数据,数据一般为两个列表（长度一致）。如果你的数据是字典或者是带元组的字典。可利用cast()方法转换,is_more_utils可以选择数据的显示方式
    bar.render(types+'.html')
    # 生成本地html文件

def main(datas,types,langzi):
    if langzi == 'wc':
        low_datas = Counter(datas).most_common(50)
        low_name  = [x[0] for x in low_datas]
        low_value = [x[1] for x in low_datas]
        run_wordcloud(low_name,low_value,types)
    if langzi == 'bar':
        name_bar = list(datas.keys())
        value_bar = list(datas.values())
        run_bar(name_bar,value_bar,types)



if __name__ == '__main__':
    data = [x.strip() for x in open('result.txt','r',encoding='utf-8').readlines()]
    jieba_wc = {'低危漏洞': [], '中危漏洞': [], '高危漏洞': [],
                '低危公司': [], '中危公司': [], '高危公司': []}
    low_company,mid_company,hig_company = [],[],[]
    # 漏洞公司名称
    for x in data:
        _ = eval(x)
        if _[2] == '低危':
            jieba_wc['低危漏洞'].append(_[1])
            jieba_wc['低危公司'].append(_[0])
        if _[2] == '中危':
            jieba_wc['中危漏洞'].append(_[1])
            jieba_wc['中危公司'].append(_[0])
        if _[2] == '高危':
            jieba_wc['高危漏洞'].append(_[1])
            jieba_wc['高危公司'].append(_[0])

    main(jieba_wc['低危漏洞'],'词云版本_低危漏洞','wc')
    main(jieba_wc['中危漏洞'],'词云版本_中危漏洞','wc')
    main(jieba_wc['高危漏洞'],'词云版本_高危漏洞','wc')


    #print(jieba.analyse.extract_tags(''.join(jieba_wc['低危公司'])))
    #print(jieba.analyse.extract_tags(''.join(jieba_wc['中危公司'])))
    #print(jieba.analyse.extract_tags(''.join(jieba_wc['高危公司'])))
    # 打印不同等级的关键词


    key_words = (jieba.analyse.extract_tags(''.join(jieba_wc['高危公司'])))+(jieba.analyse.extract_tags(''.join(jieba_wc['中危公司'])))+(jieba.analyse.extract_tags(''.join(jieba_wc['低危公司'])))

    print(key_words)
    # 打印所有的关键词
    jieba_bar = dict.fromkeys(key_words,0)
    for key_word in key_words:
        for x in data:
            _ = eval(x)
            if key_word in _[0]:
                jieba_bar[key_word] += 1
            # 所有关键词分类
            # if _[2] == '高危':
            # #如果按照不同等级分类，这里可以设置 低中高 等级
            #     if key_word in _[0]:
            #         jieba_bar[key_word] +=1

    #main(jieba_bar,'所有关键词漏洞网址','bar')





