from flask import Blueprint,request

cms_bp = Blueprint('cms',__name__,subdomain="cms")  #定义一个cms得蓝图，设置子域名位：“cms"

@cms_bp.route('/')
def Cms():                            #定义蓝图函数 获取cookie 信息，并返回
	username = request.cookies.get("username")
	return username or "没有cookie 信息"