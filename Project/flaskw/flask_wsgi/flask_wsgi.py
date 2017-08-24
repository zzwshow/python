#处理三个url 分别是
#1、GET /：首页，返回Home
#2、GET /signin:登陆页，显示登陆表单
#3、POST /signin:处理登陆表单，显示登陆结果
##同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。

from flask import Flask,render_template
from flask import request

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def Home():
	return render_template('home.html')

#浏览器get请求返回表单页面
@app.route('/signin',methods=['GET'])
def signin_form():
	return render_template('form.html')

#根据浏览器传过来的表单信息判断用户账户密码
@app.route('/signin',methods=['POST'])
def signin():
	username=request.form['username']
	password=request.form['password']
	if username=='admin' and password=='cals':
		return render_template('login_ok.html',username=username)
	return render_template('form.html',message='Bad username or password',username=username)



if __name__ == '__main__':
	app.run(debug=True,port=1000)
