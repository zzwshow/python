#coding=utf-8
#正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。

# class Student(object):
#     pass
#
# s= Student()  #定义实例
# s.name ='zzw' # 动态给实例绑定一个属性
# print(s.name)
#
# #还可以尝试给实例绑定一个方法：
# def set_age(self,age):
#     self.age=age
#
# from types import MethodType
#
# s.set_age=MethodType(set_age,s) #为实例绑定方法
# s.set_age(100) #调用实例方法
#
# print(s.age) #打印实例属性！
#
#
# #但是，给一个实例绑定的方法，对另一个实例是不起作用的：
#
# #为了给所有实例都绑定方法，可以给class绑定方法：
# #在定义一个函数方法
#
# def set_score(self,score):
#     self.score=score
#
# Student.set_score=set_score #类绑定方法
#
# s.set_score(1000)  #类实例调用方法并传入参数
# print(s.score)
#
# #通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
#
# #使用__slots__
# #但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#
# class Student():
#     __slots__=('name','age')
#
# s=Student()
# s.name='zhang'
# s.age='28'
# print(s.name,s.age)
#
# s.score='10'
# print(s.score) #会报错，因为score不在被定义的范围之内！

#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。



################################################

#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：

#这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，
# 再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：


# class student():
#     def get_score(self):
#         return self.__score
#
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an interger!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100')
#
#         self.__score=value
#
# ss=student()
# ss.set_score(90)
#
# print(ss.get_score())
#

#但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
#还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，
# 装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：

# class student_1(object):
#
#     @property              #getter方法
#     def score(self):   #将这个score变成属性！在前面加@property
#         return self.sc #定义一个属性！ 并返回
#
#     @score.setter      #setter方法！#上面已经将函数score变为属性了 这里定义一个score方法，用于判断分数value！
#     def score(self,value):   #等
#         if not isinstance(value,int):
#             raise ValueError('score must be an interger')
#         if value < 0 or value >100:
#             raise ValueError('score must between 0~100')
#         self.sc = value #判断完之后，将结果赋值给上面的self.sc 属性！并return
#
#
# #@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，
# # 只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，
# # 负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
#
# ss= student_1()
# ss.score = 10 #给属性赋值！ 执行def score(self,value):这行函数！
# print(ss.score)

#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
#根据出生年份 算出年龄！
class student_2(object):
    @property
    def birth(self):
        return self.bi

    @birth.setter
    def birth(self,value):
        if isinstance(value,int):
            self.bi = value

        raise ('value must be an integer') #如果不是整数就将字符串 返回给@property 函数！

    @property
    def age(self):
        return 2017 - self.birth
#上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
sss=student_2()
sss.birth = "1990"
print(sss.age)





