#coding=utf-8
#
# l1=['redhat','centos','ubuntu']
# for i,k in enumerate(l1):
#     print(i,k)

#
# l1 = ['烧饼',11,22,33]
# l2 = ['is',11,22,33]
# l3 = ['sb',11,22,33]
#
# r=zip(l1,l2,l3)
#
# temp=list(r)[0]
# ret=' '.join(temp)
# print(ret)
#
#
# # 两个列表合成一个字典
# keys=[1,2,3,4,5,6,7,8]
# va=['a','b','c','d','r','t','l','k']
# d= {}
#
# for k,i in zip(keys,va):
#     d[k]=i
# print(d)

#globals() 显示所有的全局变量
#locals() 显示所有局部变量
def show():
    a = 123
    b = '123'
    print(locals())
    print(globals())
show()

#callable() 判断是否可以被调用
def f1():
    pass
print(callable(f1))


a=1
print(callable(a))


#map(函数,可迭代的对象),循环第二个参数,将每一个元素执行第一个函数,就把返回值存入结果result中

l1=[11,22,33,44,55,66]
def f1(a):
    return a+100

aa=map(f1,l1)
print(aa)
print(list(aa))








