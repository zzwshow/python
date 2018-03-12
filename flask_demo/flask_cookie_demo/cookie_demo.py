from flask import Flask,render_template,Response
from Blue_models import cms_bp

app = Flask(__name__)
app.config["SERVER_NAME"] = 'hy.com:3000'  #设置主域名
app.register_blueprint(cms_bp)    #注册蓝图


@app.route('/')
def hello_world():   #设置cookie
	resp = Response('cookie_demo')
	#设置cookie 信息username和zhangzhiwei ,过期时间，cookie在子域名下可以使用！，
	resp.set_cookie("username",'zhangzhiwei',max_age=60,domain=".hy.com")
	return resp

@app.route('/del/')
def Delete_cookie():  #删除cookie
	resp = Response("delete_cookie")
	resp.delete_cookie("username")
	return resp


if __name__ == '__main__':
	app.run(debug=True,port=3000)
