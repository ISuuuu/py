# -*- coding: utf-8 -*-
import getpass
from test.double_const import PI
#name="first to write py"
###print name
###print('Hello World')
#names=raw_input("input userdi")
###print name 
#pwd = getpass.getpass("ren")
###print pwd
a=100
if a>=0:
    ##print(a)
else:
    ##print(-a)

##print 'abc\r\ndef'
##print r'\r\n'   #r''中的字符串均不转义
##print('''line1
line2
line3''')  #打印出3行

##print "a"=="A"
##print PI
##print 10/3
##print 10//3
name="中文输入"
if isinstance(name, unicode):
    ##print name.encode('utf-8')
else: 
    ##print name.decode('utf-8')
##print u'\u54c8\u54c8'  #中文正常
##print ord('A')
###print ord('中').encode('utf-8')
##print chr(86)

#############数组
classmates=['a1','a2',PI]
##print classmates
##print classmates[0]
##print classmates[-1] #索引  获取最后一个元素
classmates.append('ByAppent')
classmates.insert(0,'ByInsert')
classmates.pop(1) #删除指定的位置的元素  参数为空 删除末尾元素
##print classmates

classM=('a1','a2','a3')  #值一旦确定，就无法赋值 ,为空t=(), 
classM2=(1)  #表示int 1
##print classM2
classM3=(1,) #表示仅有一个元素

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

##print L[0][0]

str=1981
##print str
##print int(str)

sum=0
for x in [1,2,3,4,5,6,7,8,9]:
    sum+=x
##print sum

#classmates.append(range(5)) 
classM4=range(5)
for x in classM4:
    classmates.append(x)
##print classM4
##print classmates

d={'a1':88,'a2':98,'a3':60}
##print d['a1']
