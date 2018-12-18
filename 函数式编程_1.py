# ----------------------------------------------
#a = [i for i in range(10)]
#print(a)
#def mulTen(num):
#    return num * 10

# map(func, *iterables)
#results = map(mulTen, a)
#for result in results:
#    print(result, end=' ')

#l = [i for i in results]
#print(l)


# ----------------------------------------------
# reduce 案例
# 需要从 functools 包导入
#from functools import reduce
#def myAdd(x, y):
#    return x + y

#rst = reduce(myAdd, [1, 2, 3 ,4, 5, 6])
#print(rst)

# ----------------------------------------------
# filter函数 
# 过滤函数：对一组数据进行过滤，符合条件的数据会生成一个新的列表并返回。
# 调用格式　filter(func, data)
# f 是过滤函数，data 是数据

#ls = [1, 4, 5, 6, 7, 8, 0]
#def myFilter(list1):
#    return list1 % 2 == 0
#res = filter(myFilter, ls)
#res1 = filter(lambda x: x % 2 ==0, ls)
#print([i for i in res1])
#print(res1)

# ----------------------------------------------
# 返回函数
# 函数作为返回值返回，被返回的函数在函数体内定义

#def myFunc2():
#    def myFunc3():
#        print('In myFunc3')
#        return 3
#    return myFunc3

#f = myFunc2()
#print(type(f))
#print(f)
#a = f()
#print(a)


# ----------------------------------------------
# 闭包(closure)
# 当一个函数在内部定义函数，并且内部的函数使用外部函数的参数或者局部变量，当内部的函数被当做返回值的时候，相关参数和变量保存在返回的函数中，这种结构叫做闭包。

#def count():
#    fs = []
#    for i in range(1, 4):
#        def f():
#            return i * i
#        fs.append(f)
#    return fs
#f1, f2, f3 = count()
#print(f1())

#def count1():
#    def f(j):
#        def g():
#            return j * j
#        return g
#    fs = []
#    for i in range(1, 4):
#        fs.append(f(i))
#    return fs

#f1, f2, f3 = count1()
#print(f1())
#print(f2())
#print(f3())



# ----------------------------------------------
# 装饰器
# 在不改动函数代码的基础上无限制扩展函数功能的一种机制，本质上讲，装饰器是一个返回函数的高阶函数


import time
def printTime(func):
    def wrapper(*args, **kwargs):
        print("Time: ", time.ctime())
        return func(*args, **kwargs)
    return wrapper

#@printTime
#def hello():
#    print('很高兴认识你')
#hello()
#


# 手动执行装饰器
# 先定义函数

#import time 
#def outFunc(func):
#    def inFunc(*args, **kwargs):
#        print("Time ", time.ctime())
#        return func(*args, **kwargs)
#    return inFunc

def hello3():
    print('手动执行')
hello3()

hello3 = printTime(hello3)
hello3()

f = printTime(hello3)
f()

# -----------------------------------
# 偏函数
# 参数固定的函数，相当于一个有特定参数的函数体
# fcunctools.partial 的作用是，把一个函数的某些参数固定，并返回一个新函数
# import functools
# int16 = functools.partial(int, base=16)
