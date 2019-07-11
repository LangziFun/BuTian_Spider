
#__blog__:www.langzi.fun
with open('不带http的.txt','a+')as a:
	a.writelines(filter(lambda x:'http' not in x ,[x.lstrip() for x in list(set(open('srcname技巧寻找.txt','r').readlines()))]))
	#a.writelines(filter(lambda x:'edu.cn'  in x or 'gov.cn'  in x,[x.lstrip() for x in list(set(open('alive_urllll.txt','r').readlines()))]))


