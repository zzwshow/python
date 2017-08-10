#coding=utf-8

import os,sys


project_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_path)
print(os.path.dirname(os.path.abspath(__file__)))
#__file__ 返回程序本身名字

print(sys.argv) #命令行参数，第一个元素是程序本身路径
#sys.exit(n)  #退出程序，正常退出时exit(0)
print(sys.maxsize) #最大的Int值
print(sys.platform) #返回系统平台
print(sys.stdin) #

#
# line=sys.stdin.readline().strip() #标准输入 去掉‘\n’
# for i in range(len(line)):
#     print(line[i]+'HELLO')
#
# print(len(line))



#进度条示例：
import time
def view_num(num,total):
    rate=num / total
    rate_num=int(rate * 101)
    r='\r%s%d%%' %(">"*num,rate_num)
    sys.stdout.write(r)
    sys.stdout.flush()

# if __name__ == '__main__':
#     for i in range(0,101):
#         time.sleep(0.1)
#         view_num(i,101)






