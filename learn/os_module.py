#coding=utf-8
import os
print(os.getcwd())
#C:\Users\cals\Desktop\python\FLASK\learn3.5
#获取当前文件所在的完整目录路径
#os.chdir()
print(os.curdir)
print(os.pardir)
#os.makedirs('dir1/dir2') #递归创建目录
#print(os.removedirs('dir1/dir2')) #递归删除目录，若目录为空继续向上递归

#os.mkdir('dir1') #创建单级目录
#os.rmdir('dir1') #若单级目录为空则删除 不为空报错

#os.chdir('dir1/dir2')

#先切换到'dir1/dir2' 目录，然后列出目录内容！


print(os.path.abspath(os.path.dirname(os.pardir)))
#返回path规范化的绝对路径






