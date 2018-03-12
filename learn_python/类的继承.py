#coding=utf-8

#类的继承
# 1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
# 2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
# 3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。

#如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。

class Parent:
    parentAttr=100
    __age=77         #类的私有属性只能类内部使用！只能是允许这个类本身进行访问了。
    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print("调用父类方法")
        print(self.__age)
    def setAttr(self,attr):
        Parent.parentAttr=attr

    def getAttr(self):
        print("父类属性：",Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print("调用子类构造方法 child method")


print(Parent.parentAttr) #打印类属性
#print(Parent.__age)    #外部无法调用私有类属性

c=Child()                 # # 实例化子类
print(c.childMethod())  # 调用子类的方法
print(c.parentMethod())   # 调用父类方法
c.setAttr(200)          # 再次调用父类的方法 传参数进去
print(c.getAttr())  # # 再次调用父类的方法 获取传进去的参数










