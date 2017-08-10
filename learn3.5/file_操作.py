#coding=utf-8
#utf-8 :一个汉字3个字节
# #gbk:一个汉字2个字节
# #1字节等于8比特（bit）
# #
# #字符串转换字节类型：bytes(只要转换的字符串,按照什么编码)
# s="张志伟"
# n = bytes(s,encoding="utf-8")
# print(n)
#
# #字节转换为字符串（转换上面的n）
# new_str=str(n,encoding="utf-8")
# print(new_str)
#
# #open 打开文件
# # 需要三个步骤
# #    1、打开文件
# #    2、操作文件
# #    3、关闭文件
#
# #每次都要关闭文件比较麻烦，可以使用，with open('文件路径’,'打开模式') as filename: 这种方式来打开文件
#
# aa=open('aa.txt','r',encoding='utf-8')
# data=aa.read()
# aa.close()
# print(data)
#
# #用with语句打开，不需要手动关闭
# with open('aa.txt','r',encoding="utf-8") as f:
#     print(f.read())
#
# f = open('aa.txt','r',encoding="utf-8")
# print(f.encoding)
#
# ff=f.read()
# f.close()
# print(f.closed) #判断文件是否关闭

#读取一个文件中的10行写入另外一个文件中
# with open('aa.txt','r',encoding='utf-8') as f1,open('cc.txt','w',encoding='utf-8') as f2:
#     times = 0
#     for i in f1:
#         times += 1
#         if times <= 5:
#             f2.write(i)
#         else:
#             break

# import os
# import os.path
# filename='C:/Users/cals/Desktop/python/flask/learn3.5/test.txt'
# if os.path.isfile(filename):
#     f1=open(filename,'a+')
#
# with True:
#     line=input('Please input:')
#     if line == 'q' or line == 'exit':
#         break
#     f1.write(line+'\n')
# f1.close()



# 示例：判断文件是否存在，存在则打开
# 让用户通过键盘反复输入多行数据
# 追加保存至此文件中
# import os
# import os.path
#
# filename = 'C:/Users/cals/Desktop/python/flask/learn3.5/test.txt'
#
# if os.path.isfile(filename):
#     with open(filename,'a+',encoding='utf-8') as fff:
#         while True:
#             line = input('Enter somethin> ')
#             if line != 'q' or line != 'quit':
#                 fff.write(line+'\n')
#             else:
#                 break





































