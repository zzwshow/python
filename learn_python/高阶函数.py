#coding=utf-8

#map() and reduce()

#map()函数接收两个参数，
# 一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回。

#求数字5的任意次幂
def f(x):
    return 5 ** x
print(f(2)) #2次幂


l=map(f,[3,])  #3次幂
print(list(l))
# map()传入的第一个参数是f，即函数对象本身。
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

#将整数变换为字符串
aaa=list(map(str,[1,2,3,4,5,6,7,8]))
print(aaa)


#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

from functools import reduce
def add(x,y):
    return x+y

ll=reduce(add,[1,2,3,4])
print(ll)


