from flask import Flask,session
import os
app = Flask(__name__)
#设置SECRET_KEY 为了加密session
app.config['SECRET_KEY']= os.urandom(24)

#添加数据到session
#操所session 和操作字典是一样的
#session需要设置SECRET_KEY（用来加密）

#定义session
@app.route('/')
def hello_world():
	session['username']='admin'
	return 'Hello World!'

#获取session和字典一样两种方法（1、session['username']）
#（2、session.get('username')）第一种若session不存在会返回错误信息
#第二种会会返回None

@app.route('/get/')
def get():
	return session['username']

#删除某一个session(先获取 然后删除 在获取一下验证)
@app.route('/delete')
def delete():
	print(session.get('username'))
	session.pop('username')
	print(session.get('username'))
	return "success"

#全部删除session
@app.route('/clear')
def clear():
	print(session.get('username'))
	session.clear()
	print(session.get('username'))
	return "success"

if __name__ == '__main__':
	app.run(debug=True,port=1000)
