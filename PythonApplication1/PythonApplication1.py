# -*- coding: utf-8 -*-
import getpass
from test.double_const import PI
#name="first to write py"
#print name
#print('Hello World')
#names=raw_input("input userdi")
#print name 
#pwd = getpass.getpass("ren")
#print pwd
a=100
if a>=0:
    print(a)
else:
    print(-a)

print 'abc\r\ndef'
print r'\r\n'   #r''中的字符串均不转义
print('''line1
line2
line3''')  #打印出3行

print "a"=="A"
print PI
print 10/3
print 10//3
name="中文输入"
if isinstance(name, unicode):
    print name.encode('utf-8')
else: 
    print name.decode('utf-8')
print u'\u54c8\u54c8'  #中文正常
print ord('A')
#print ord('中').encode('utf-8')
print chr(86)

#############数组
classmates=['a1','a2',PI]
print classmates
print classmates[0]
print classmates[-1] #索引  获取最后一个元素