from flask import Flask,session
import os
from datetime import timedelta


app = Flask(__name__)
app.config['SECRET_KEY']= os.urandom(24)  #用于给session加盐
#app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)
#定义session两个小时过期


@app.route('/')    #生成session
def hello_world():
	session["username"] = "zhangzhiwei"
	session.permanent=True    #设置三十天过期。
	return "hello world"


@app.route("/get_session/")   #获取session
def Get_session():
	username = session.get("username")
	return username or "没有session"


@app.route("/del_session/")   #删除session
def Del_session():
	session.pop("username")    #删除某个session
	#del session["username"]   #删除某个session
	#session.clear()         #删除所有session
	return "session 已经删除"


if __name__ == '__main__':
	app.run(debug=True,port=9000)
