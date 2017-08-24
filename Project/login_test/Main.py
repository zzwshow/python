#coding=utf-8
__author__='zzw'

import getpass as gp
import pickle
import os

if not os.path.exists("C:\Users\cals\Desktop\python\Project\login_test\lock_user.txt"):
	lock_user_file=open('lock_user.txt','wb')
	lock_user=[]
	pickle.dump(lock_user,lock_user_file)
	lock_user_file.close()
	
_username='zzw'
_password='zhangzhiwei'

inpu_user={}
count=0
while count<3:
	print('第{}次输入'.format(count+1))
	username=input("username:")
	if username not in inpu_user:
		inpu_user[username]=0
	lock_user_file=open('lock_user.txt','rb')
	lock_user=pickle.load(lock_user_file)
	lock_user_file.close()
	