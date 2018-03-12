

#1、类继承  问：如何调用类A的show方法了。
# class A():
# 	def show(self):
# 		print("base show")
#
#
# class B(A):
# 	def show(self):
# 		print("derived show")
#
# obj = B()
# obj.show()
#
# #答：
# obj.__class__ = A
# obj.show()

#__class__方法指向了类对象，只用给他赋值类型A，然后调用方法show


#2、方法对象
#问题：为了让下面这段代码运行，需要增加哪些代码？

# class A():
# 	def __init__(self,a,b):
# 		self.__a = a
# 		self.__b = b
#
# 	def myprint(self):
# 		print('a=',self.__a,'b=',self.__b)
#
# 	def __call__(self, num):
# 		print('call:',num+self.__a)










