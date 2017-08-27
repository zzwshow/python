from flask import Flask,render_template,request,session

app = Flask(__name__)

#before_request :在视图函数请求之前
#它只是一个装饰器，
# 他可以把需要设置为钩子函数的代码放到试图函数前执行！

@app.route('/')
def index():
	print('index')
	return 'index'

@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return render_template('login.html')
	else:
		username=request.form.get('username')
		password=request.form.get('password')
		if username == 'admin' and password == 'admin':
			session['username'] = 'admin'  #将admin用户加入session 保存用户登陆状态
			return u'登陆成功！'
		else:
			return u'用户名或密码不存在'


@app.route('/edit/')
def edit():
	if session.get('username'): #判断用户是否登陆
		return u'修改成功'
	else:
		return u'请先登陆'

#定义钩子函数：可所有试图函数执行之前先执行下面的钩子函数
# 会先打印‘before_request’ 然后在打印出‘hello world’
@app.before_request
def my_before_request():
	print('before_request!')


if __name__ == '__main__':
	app.run()






