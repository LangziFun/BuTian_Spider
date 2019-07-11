#__blog__:www.langzi.fun
with open('带http的.txt','a+')as a:
	a.writelines(filter(lambda x:'http'  in x ,[x.lstrip() for x in list(set(open('URLS.txt','r').readlines()))]))


with open('不带http的.txt','a+')as a:
	a.writelines(filter(lambda x:'http' not in x ,[x.lstrip() for x in list(set(open('URLS.txt','r').readlines()))]))
