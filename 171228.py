#coding:utf-8
# 列表生成式 
# isinstance

arrK=[x*x for x in range(1,11)]
print (arrK)
arrK=[x*x for x in range(1,11) if x%2==0]
print (arrK)

import os 
arrDir=[d for d in os.listdir('..')]  # 列出 os.listdir中文件和目录

print  (arrDir)
arrDirChinese=[]

for x in arrDir:
    arrDirChinese.append(str(x))
    pass

print (arrDirChinese)
s='\u9738\u738b\u522b\u59ec'   #转成中文 u'\u9738\u738b\u522b\u59ec'

print (s)

#字典中
d={'x':'xvalue','y':'yy','z':'hah'}
for x,y in d.items():
    print(x,'==',y)

da=[k+'='+v for k ,v in d.items()]
daa=[s.upper() for s in da]  #转大写
print (daa)
print (da)

#exercise

L=['Hello','zhangsan','张三',18,'lal','qwe']
LUpper=[]
def toUpper():
    for x in L:
        if isinstance(x,str):  #isinstance 判断是否是某类型
            LUpper.append(x.upper())
        else:
            LUpper.append(x)
            pass


toUpper()

print (LUpper)

