zjl ='迭代'
#如果给定一个list 或tuple 我们通过for 循环遍历这个list或tuple 这种遍历我们称为 迭代（iteration）
#在Python 中 迭代时通过for...in 来完成的

d={'a':'1','b':'2','c':'3'}
for i in d:
    print i
for i in d.values():
    print i
for k,v in d.items():  #获取d中values值
    print k+":"+v  

for ch in 'zhangsan':
    print ch

n='zhangsan'
print n[::2]  

#通过collections模块的Iterable类型判断一个对象是否是可迭代对象

from collections import Iterable

print  isinstance('abc',Iterable)  #返回 True or False

#如果对list实现下标循环，
for i,b in enumerate(['A','B','C']):
    print(i,b)
    
for x,y in [(1,2),(2,4),(4,8)]:
    print (x,y)





#因为dict的存储不是按照list的方式顺序排序，所以，迭代出的顺序很可能不一样