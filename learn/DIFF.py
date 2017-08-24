#coding=utf-8

import difflib

import sys
try:
    textfile1=sys.argv[1] #获取第一个参数
    textfile2=sys.argv[2] #获取第二个参数
    print(textfile1,textfile2)
except Exception as e:     #捕捉参数异常
    print('Error:'+str(e))
    print('Usage: DIFF.py filename1 filename2')
    sys.exit()
def readfile(filename):  #定义函数，以行为分割
    try:
        fileHandle = open(filename,'rb')  #以二进制方式读取文件内容
        text=fileHandle.read().splitlines() #生成行为分割的对象
        fileHandle.close()
        return text                       #返回
    except IOError as error:            #捕捉读取异常
        print('Read file Error:'+str(error))
        sys.exit()
if textfile1 == "" or textfile2 == "":  #判断文件是否为空
    print("The file cannot be empty!!!")
    sys.exit()
else:
    text1_lines=readfile(textfile1)  #调用函数并定义一个以行为分割的文件对象
    text2_lines=readfile(textfile2)

d=difflib.HtmlDiff() #定义以HtmlDiff()方法进行比较的对象
print(d.make_file(text1_lines,text2_lines)) #掉用对象的make_file()方法生成HTMl文件



