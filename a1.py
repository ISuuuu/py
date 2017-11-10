sa="张三"
print sa

def my_abs(x):
    if x>=0:
        return x
    else:
         return -x

print my_abs(10)   

def fa(n):  
    if n==1:
        return 1
    return n*fa(n-1)

print fa(4)

sType ="解决递归调用栈溢出的方法时通过尾递归优化，"
sType="尾递归是指在函数返回的时候，调用自身本身，并且，return 不能包含表达式"
sType="这样，递归无论调用多少次，都只用只用一个栈，不会出现内存溢出的情况"



def fact(n):
    return facr_iter(n,1)

def facr_iter(num,product):
    if num==1:
        return product
    return facr_iter(num-1,num*product)

print fact(5)  

L=[]
n=1
while n<=99:
    L.append(n)
    n+=2

print L[0]

ina=len(L)






