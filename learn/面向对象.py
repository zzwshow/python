#coding=utf-8

class A:
    def __init__(self,name): #构造函数，初始化数据
        self.name=name #封装数据
    def f1(self):
        print(self.name) #通过self间接获取封装的数据

a= A('zzw')
print(a.name)
a.f1()

class A:
    name='zzw'
    __age=18
    def __init__(self):
        self.__like__='zhang'
        self.hobby='kkkk'
    def f1(self):
        print(self.__age)
        print(self.__like__)

a = A()
a.f1()
print(a.hobby)




