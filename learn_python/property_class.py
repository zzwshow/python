

# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
#
# s = Student()
# s.score = 9999
# 这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：

#@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
# class Student(object):
#
# 	@property
# 	def score(self):
# 		return self._score
#
# 	@score.setter
# 	def score(self,value):
# 		if not isinstance(value,int):
# 			raise ValueError('score must be an integer')
# 		if value < 0 or value > 100:
# 			raise ValueError('score must between 0~100')
# 		self._score = value
#
#
# a = Student()
# a.score=10
# print(a.score)



def foo(s):
	n = int(s)
	assert n != 0,'n is zero'
	return 10/n

def main():
	foo('0')





