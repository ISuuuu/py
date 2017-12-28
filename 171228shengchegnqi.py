#
#生成器 generator
#要创建一个generator有很多中方法 第一种 把列表生成式中的[]改成() 即可


L=[x*x for x in range(10)]
print (L)

g=(x*x for x in range(1,11)if x%2==0)

#print (g)
print (next(g))   #基本上不会使用
 #generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。


# for x in g:
#     print (x)  

def test(max):
    n,a,b=0,0,1
    x,y,z=0,9,[9,1]
    print (y)

test(2)

print('----------------')
#斐波拉基数列
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done_1'

#fib(7)  
print('----------------')
def fib_new(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'dd'
#如果一个函数包含了yield 关键字  这就是一个generator

for x in fib_new(6):
    print (x)

print('----------------')

def odd():
    yield 1
    yield 2
    yield 3

odd()
#?????????

