from flask import g

def login_log():
	print('当前登陆用户是：%s' % g.username)