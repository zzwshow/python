#coding=utf-8
def genNum(x):
    y=0
    while y <= x:
        yield y
        y+=1

aa=genNum(5)
print(next(aa)) #取出第一个迭代对象！

print(type(aa))
for i in aa:
    print(i)

#加上yield 为返回值 可一得到一个迭代器！



