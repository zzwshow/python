#coding=utf-8

import re
#findall()可以将匹配到的结果以列表的形式返回，如果匹配不到则返回一个空列表
def re_method():

    s1='Hello this is joey'
    s2='The first price is $9.90 and the second price is $100'
    print(re.findall(r'\w',s1)) #[a-z-A-Z-0-9]
    print(re.findall(r'\d+\.?\d*',s2))

#finditer() 可以将匹配到的结果生成一个迭代器
def re_method1():
    s2='The first price is $9.90 and the second price is $100'
    s = re.finditer(r'\d+\.?\d*',s2)
    for i in s:
        print(i.group())  #



#search() 是匹配整个字符串直到匹配到一个就返回
def re_demo():
    txt='If you puchase more than 100 sets, the price of product A is $9.90.'
    m = re.search(r'(\d).*\$(\d+\.?\d*)',txt)
    print(m.groups())

#match从要匹配的字符串的开头开始，尝试匹配，如果字符串开始不符合正则表达式，则匹配失败，
# 函数返回None,匹配成功的话用group取出匹配的结果
def re_method2():
    s='abcdc'
    print(re.search(r'c',s)) #seach是从头到尾的匹配 第一个匹配
    print(re.search(r'^c',s)) #匹配开头为c 没有匹配到返回None
    print(re.match(r'c',s)) #相当于^c开头匹配 没有匹配到返回None
    print(re.match(r'.*c',s))

def re_method_object():
    s1='Joey Huang'
    m = re.match(r'(.*?) (\w+)',s1)
    print(m.group(1,2))
    print(m.groups())
#split能够将匹配的子串分割后返回列表
def re_method_split():
    s1='This is joey Huang'
    print(re.split(r'\W',s1))

#re.sub()、re.subn()
#sub能将匹配到的字段用另一个字符串替换返回替换后的字符串，
# subn还返回替换的次数
def re_method3():
    s2='The first price is $9.90 and the second price is $100'
    print(re.sub(r'\d+\.?\d*','<number>',s2,1))# 还能指定替换的次数 这里是1次
    print(re.subn(r'\d+\.?\d*','<price>',s2))


#if __name__ == "__main__":
    #re_method()
    #re_method1()
    #re_demo()
    #re_method2()
    #re_method_object()
    #re_method_split()
    #re_method3()

#re的flags标识位
def re_pattern_syntax():
    # .表示任意单一字符
    # *表示前一个字符出现>=0次
    # re.DOTALL就可以匹配换行符\n,默认是以行来匹配的
    print(re.match(r'.*', 'abc\nedf').group())
    print('*' * 80)
    print(re.match(r'.*', 'abc\nedf', re.DOTALL).group())


if __name__ == '__main__':
    re_pattern_syntax()










#小例
# print(re.match('www','www.baidu.com').span()) #从字符串开头开始匹配 返回匹匹配的字符串跨度
#
# print(re.match('www','www.baidu.com')) #匹配成功返回匹配对象
# print(re.match('com','www.baidu.com')) #文件开头没有匹配成功，返回None
#
# print(re.search('www','www.baidu.com').span())
# print(re.search('com','www.baidu.com').span())
# #re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，
# # 函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
#
# phone='18839399820 ￥这个号码值5元'
# print(re.sub(r'￥.*$','',phone))#将￥符号后所有字符替换为空‘’
# print(re.sub(r'\D','',phone)) #将非数字的替换为空！
# # answer:
# # 18839399820
# # 188393998205
#
#
# #

