
#递归1
def f(n):
    if n == 0: # n=0 的话直接返回空，对用户输入的零进行判断
        return None
    elif n == 1:   # n=1 的话就不再递归
        return n
    else:
        return n*f(n-1)    # 递归在执行f(n-1) 直到f（1）

print(f(5))

#递归2
def func(n):
    n += 1
    if n >=4:
        return 'end'
    return func(n)
r = func(1)
print(r)
#练习
#1、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
def fun(s):
    Digitnum,Alphanum,Sapcenum,Othernum=0,0,0,0
    for i in s:
        if i.isdigit():
            Digitnum += 1
        elif i.isalpha():
            Alphanum += 1
        elif i.isspace():
            Sapcenum += 1
        else:
            Othernum += 1

    return Digitnum,Alphanum,Sapcenum,Othernum

aa = fun('zzw 27 ""')
print(aa)

#2写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5　(大于为True)
def f(s):
    ret=False
    if isinstance(s,str) or isinstance(s,list) or isinstance(s,tuple):
        if len(s) >5:
            ret = True
        return ret

print(f('zhan'))
print(f([1,2,3,4,5,6]))
print(f(('a','b',3,'d','kk','oo')))

#3 写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容 (不包含为True)
def fun(s):
    ret=False
    if isinstance(s,str) or isinstance(s,list) or isinstance(s,tuple):
        for i in s:
            if i == ' ':
                ret=True
                break
    return ret

#4写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def fun(s):
    if isinstance(s,list):
        if len(s) >2:
            return s[0:2]
    return None
print(fun([1,2,3,4,5]))

#5写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。

def f(s):
    if isinstance(s,list) or isinstance(s,tuple):
        l=[]
        for i in range(0,len(s),2):
            l.append(s[i])
        return l
    return None
ll=f([1,2,3,4,5,6,7,8,9])
print(ll)


#6、写函数，检查传入字典的每一个value的长度,如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者。
print('-------------------------------')
def fun(s):
    if isinstance(s,dict):
        for i in s:
            if len(s[i])>2:
                s[i]=s[i][0:2]
    return s


s={'a':'llll','b':'jjjjj','c':'123'}
ss=fun(s)
print(ss)
















