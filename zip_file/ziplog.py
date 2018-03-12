#coding=utf-8

import os
import shutil  #移动文件到执行目录时要用
from time import strftime #用于设置当前系统时间！

logsdir="C:\Users\cals\Desktop\python\Project\zip_file\logs"
zipdir="C:\Users\cals\Desktop\python\Project\zip_file\logs\zip_dir"
zip_command="7za a"

for files in os.listdir(logsdir):  #列出日志目录下的说有文件！
	if files.endswith('.log'): #找到以.log结尾的文件
		files1=files+'.'+strftime("%Y-%m-%d")+".zip" #设置压缩后文件名！
		os.chdir(logsdir)                          #切换到被压缩文件的目录下
		os.system(zip_command+' '+files1+' '+files) #执行压缩命令
		shutil.move(files1,zipdir)  #将压缩后的文件移动到zip_dir目录中
		#os.remove(files)         #删除源文件
		
		
	












