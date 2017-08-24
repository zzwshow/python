#文件操作
#format

a = 'I am {0},My age {1}'.format('zzw',28)
print(a)


a1= 'I am {0},My age {1}'.format(*['zzw',28])
print(a1)


a2='I am {0},My age {1}'.format(*('zzw',28))
print(a2)


a3='I am {name},My age {age}'.format(name='zzw',age=28)
print(a3)


dic={'name':'zzw','age':28}
a4='I am {name},My age {age}'.format(**dic)
print(a4)

# 执行方式二：执行函数时有*,
# 把所有迭代对象拆分为单个元素作为元组的元素,如传入列表,会把列表中每一个元素遍历添加到元组中当作一个元素


tp1='I am %s' % 'tomcat'
print("1",tp1)
tp1='I am %(name)s,age %(age)d' % {'name':'tomcat','age':18}
print("2",tp1)
tp1='I am %(pp).2f' %{'pp':123.456789}
print("3",tp1)



tp1="I am {},age {},{}".format('zzw',18,'hello')
print(tp1)

tp1='I am {} ,age {}'.format(*['zzw',18])
print(tp1)

tp1="I am {0},age {1}".format(*['zzw',18])
print(tp1)
tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print(tpl)