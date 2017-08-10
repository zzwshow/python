#coding=utf-8


class Dog:

    def __init__(self,name):
        self.name = name
    @staticmethod   #静态方法。。。这个函数与类就没有关系了
    def eat(self):
        print('%s is eating %s'%(self.name,food))


aa=Dog('zzw')
print(aa.eat())













