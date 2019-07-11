# coding:utf-8

print('                    \n文本去重复工具\n')

inp = input('SET YOU TARGET TEXT:')

res1 = list(([x.strip() for x in open(inp,'r',encoding='utf-8').readlines()]))
res2 = list(set([x.strip() for x in open(inp,'r',encoding='utf-8').readlines()]))

print('去重前总行数:{}\n'.format(len(res1)))
print('去重后总行数:{}'.format(len(res2)))

with open(inp+'.txt','a+',encoding='utf-8')as a:
    for ii in res2:
        a.write(ii + '\n')

print('去重完毕~')

import os
os.system('pause')