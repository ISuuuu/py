# 数组倒叙  arrL.reverse()
#  enumerate 数组中需要用到下标时  for x,y in enumerate(arr[])  x下标 y值

def excLx(str1, str2):
    return str1+str2
    pass

print (excLx(11,12))

print (excLx("zhang","san"))

print ('------------------')

L= list(range(1,5)) # 1 2 3 4

print (L)
print (sum(L))
#生成 1 -10 平方和

La=[]

#运算 求 1--9的平方和
def getHe():
    for x in range(1,10):
        La.append(x*x)     
    return sum(La)

print (getHe())

arrK =[x*x for x in range(1,10)]
print (arrK)
#写列表生成式时，把要生成的元素 x*x放在前面，后面跟for循环，就可以把list创建出来    
arrL=[x+2 for x in arrK]
print (arrL)
#能不能倒叙  先将数组反转
arrL.reverse()
print (arrL)

#以下得出的是 两数组每一项的和
# arrKL=[x+y for x in arrK for y in arrL]
# print arrKL

arrAll=[]
arrLReverse=arrL
# arrLReverse.reverse()  址传递

#能否对应项相加
def getSum():
    for x,xvalue in enumerate(arrL):
        for y,yvalue in enumerate(arrLReverse):
            if x==y:
                 arrAll.append(xvalue+yvalue)
            else:
                pass

getSum()
print (arrAll)








