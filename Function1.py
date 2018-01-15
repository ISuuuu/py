f =abs(-100)
fa=abs  #函数可以指向变量

print (f)
print (fa)

def addFa(x,y):
    return x+y

def add(x,y,add_Fa):
    return add_Fa(x,y)

print (add(1,5,addFa))

def fx(x):
    return x*x

r=map(fx,[1,2,3,4,5,6])
print (list(r))

a=[1,2,3,4,5,6,7]

print (list(map(str,a)))
