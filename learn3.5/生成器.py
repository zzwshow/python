#coding=utf-8

# f = open('db','r')
# for line in f:
#     line_list=line.strip().split('|')
#     print(line_list)

#函数返回一个生成器
#示例：使用yield函数生成器，能够用next()调用或for循环使用
# def genNum(x):
#     y=0
#     while y <= x:
#         yield y
#         y+=1
#
# a = genNum(5)
# for i in a:
#     print i

#示例：求1到10的平方，可以使用列表解析或者生成器，也可以是用yield

# def genNum():
#     i = 1
#     while i<=10:
#         yield i **2
#         i+=1
# aa=genNum()
# for i in aa:
#     print i

ll=[1,2,3,4,5]
aa=[i **2 for i in ll]
print aa

bb = [i **2 for i in ll if i >3]
print bb

cc = [(i**2)/2 for i in range(1,11)]
print cc


import os

filelist1=os.listdir('C:\\Users\\cals\\Desktop\\python\\flask\\learn3.5')
filelist2=[i for i in filelist1 if i.endswith('txt')]
print filelist2

l1=[1,2,3]
l2=['a','b','c']
l3 = [(i,j) for i in l1 for j in l2]
print l3


for j in (i**2 for i in range(1,11)):print (j/2)

