#coding=utf-8
# #定义一个装饰器 用来添加函数的描述信息！
# def document_it(func):
# 	def new_function(*args,**kwargs):
# 		print('Running function:',func.__name__)
# 		print('Positional arguments:',args)
# 		print('keyword arguments:',kwargs)
# 		result = func(*args,**kwargs)
# 		print('Result:',result)
# 		return result
# 	return new_function
#
# #@符号调用
# # @document_it
# # def add_int(a,b):
# # 	return a+b
# #
# # print(add_int(4,5))
#
# #手动调用
# # cooler_add_ints=document_it(add_int)
# # print(cooler_add_ints(3,5))
#
# #####在定义一个装饰器，用来求结果的平方！
# def square_it(func):
# 	def new_function(*args,**kwargs):
# 		result=func(*args,**kwargs)
# 		return result * result
# 	return new_function
#
# #调用两个装饰器！会先执行靠近def的装饰器！
# @square_it
# @document_it
# def add_int(a,b):
# 	return a+b
#
# print(add_int(3,3))
#
# ###装饰器带有参数！

def decorator_agument(text):  #接受装饰器的参数！
	def decorator_func(func):  #接收将要被装饰的函数
		def new_function(*args,**kwargs): #定义一个新的函数，并添加打印功能！可以接受任何参数！
			print('%s ---%s()'%(text,func.__name__))
			return func(*args,**kwargs) #返回传入进来的函数和参数！
		return new_function #返回添加新功能后的函数对象
	return decorator_func #返回装饰后的函数对象！

@decorator_agument('execute')
def add_inits(a,b):
	return a*b

print(add_inits(3,3))
















