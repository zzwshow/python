#coding=utf-8
class Employee:
    '所有员工的基类'
    empCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount +=1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name:",self.name,",Salary:",self.salary)


emp1=Employee('ZZW',1000)
emp2=Employee('www',2000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d"% Employee.empCount)

#emp1.age = 7  # 添加一个 'age' 属性
# emp1.age = 8  # 修改 'age' 属性
# del emp1.age  # 删除 'age' 属性

#你也可以使用以下函数的方式来访问属性：
print(getattr(emp1,'name')) #获取name属性！
print(hasattr(emp1,'name'))  #判断实例是否存在‘name'属性！
print(delattr(emp1,'salary')) #删除实例属性！
print(hasattr(emp1,'salary')) #确定是否删除 返回False

setattr(emp1,'age',8) #给实例定义新属性’age'并且值为8 ！
print(emp1.age)

#Python内置类属性

print(Employee.__dict__)
#类的属性（包含一个字典，由类的数据属性组成）
print(Employee.__doc__)
#类的文档字符串

print(Employee.__name__)
#类名

print(Employee.__bases__)
#类的所有父类构成元素（包含了一个由所有父类组成的元组）
















