#coding=utf-8

import random
print(random.random()) #生成一个0-1之间的随机小数
print(random.randint(1,10)) #生成一个1-10之间的随机整数
print(random.uniform(10,20)) #生成一个10-20之间的随机浮点数
print(random.randrange(0,10,2)) #生成1到10的整数不包括10,第3个参数可以指定步长
a=['a','b','c','d','e']
print(random.choice(a)) # 从序列中随机选一个


# 每次对序列随机排序
p = ["Python", "is", "powerful", "simple"]
random.shuffle(p)
print(p)

#########随机验证码

li=[]
for i in range(6):
    r=random.randint(0,4)
    if r == 2 or r == 4:
        num=random.randrange(0,10)
        li.append(str(num))
    else:
        temp=random.randrange(65,91)
        c=str(temp)
        li.append(c)
print(li)
result="".join(li)
print(result)






