#装饰器
from flask import session,redirect,url_for
from functools import wraps #防止装饰器更改函数的__name__

##登录限制(装饰器)
def login_required(func):
    @wraps(func) #包裹函数，防止更改__name__
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)  #如果已经登录就执行函数
        else:
            return redirect(url_for('login')) #否则返回登录页面
    return wrapper