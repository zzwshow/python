from  flask import session,redirect,url_for
from functools import wraps

#登陆限制
def Login_Required(func):

	@wraps(func)
	def inner(*args,**kwargs):
		if "user_id" in session:
			return func(*args,**kwargs)
		else:
			return redirect(url_for("cms.index"))
	return inner


