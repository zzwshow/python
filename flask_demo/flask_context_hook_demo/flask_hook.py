from flask import Flask,render_template,request,session
import os


app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)

#context_processor: 上下文处理器。解决两个页面都需要同一个数据-如下：
#定义登录后的首页
@app.route('/')
def index():
	#return render_template('index.html',username='zhangzhiwei')
	return render_template('index.html') #使用context_processor 后就不需要单独返回‘username'了

#定义登录后编辑页面
@app.route('/edit/')
def edit():
	#return render_template('edit.html',username='zhangzhiwei')
	return render_template('edit.html')

#以上两个页面都需要‘username’这里是用户登录的名称！因为只要是登录的用户就会存在’username'
#可以使用context_processor，将username返回！只要页面中有'{{ username }}' 的都会接收到！并显示在页面中！
@app.context_processor
def my_context_processor():
	# username = session.get('username') #从session中获取username(只有登录后再可以)
	# if username:
	# 	return {'username':username}

	# 这里测试直接返回了（去掉了判断没有经过下面的'login'函数)(可以看到index.html和edit.html都收到了username）
	return {'username':'zhangzhiwei'}


#登录页面
@app.route('/login',methods=['GET','POST'])
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


# 在所有视图函数执行之前执行！
# @app.before_request
# def my_before_request():
# 	return login()


if __name__ == '__main__':
	app.run(debug=True)






