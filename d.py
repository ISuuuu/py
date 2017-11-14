zjl ='迭代'
#如果给定一个list 或tuple 我们通过for 循环遍历这个list或tuple 这种遍历我们称为 迭代（iteration）
#在Python 中 迭代时通过for...in 来完成的

d={'a':'1','b':'2','c':'3'}
for i in d:
    print i
for i in d.values():
    print i
for k,v in d.items():
    print k+":"+v  

for ch in 'zhangsan':
    print ch

n='zhangsan'
print n[::2]  

#通过collections
    




#因为dict的存储不是按照list的方式顺序排序，所以，迭代出的顺序很可能不一样