from flask import Flask,session
import os
app = Flask(__name__)
#设置SECRET_KEY 使用24为随机数-用来加密session
# （因为是随机的所以服务器重启后就找不到之前加密过的session了）
app.config['SECRET_KEY']= os.urandom(24)


#添加数据到session
#操所session 和操作字典是一样的
#session需要设置SECRET_KEY（用来加密）

#定义session
@app.route('/')
def hello_world():
	session['username']='admin'
	return 'Hello World!'

#获取session和字典一样有两种方法（1、session['username']）
#（2、session.get('username')）第一种若session不存在会返回错误信息
#第二种会会返回None，不会抛出异常！

@app.route('/get/')
def get():
	return session['username']

#删除某一个session(先获取 然后删除 在获取一下验证)
# （两种方法1、session.pop('username')2、session.clear()）
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
