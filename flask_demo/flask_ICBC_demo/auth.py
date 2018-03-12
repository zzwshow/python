from functools import wraps
from flask import session,redirect,url_for



def LoginRequired(func):   #登陆限制装饰器
	@wraps(func)
	def wrapper(*args,**kwargs):
		user_id = session.get('user_id')
		#从session中获取user_id,也就是session_id 就证明用户在登陆状态，user_id不存在就返回到登陆页面
		if user_id:
			return func(*args,**kwargs)
		else:
			return redirect(url_for("login"))

	return wrapper




