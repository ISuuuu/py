L=['a1','a2','a3','a4']

##print L
##print L[0]+L[2]+L[1]

#取前n个元素可以循环读取
r=[]
n=10
for i in range(n):
    r.append(i)   

###print r
##PYTHON 中提供了切片操作符 
##print r[0:len(r)]
##print r[:3]
##print r[-1]   # 取倒数第一个元素
##print r[-2]   #后几个元素
##print r[:10:3]  #前是个元素中每隔 3个取一个 
##print r[:]   #显示所有的元素

n='abcdefghijklmnopqrstuvwxyz'
##print n[:5] 
##print n[5:6]  # n[m,n]从m开始截图n-m个长度字符   (似乎 n>m)
