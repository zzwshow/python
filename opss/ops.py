#coding=utf-8
from flask import Flask,render_template,request,redirect,url_for,session
from models import User,Hosts,Project
import config
from exts import db
from functools import wraps

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
###app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@app.route('/websocket/')
def Get_logs():
	return render_template('socket_logs.html')


#用户限制
def Login_required(func):
	@wraps(func)
	def wrapper(*args,**kwargs):
		if session.get('user_id'):
			return func(*args,**kwargs)
		else:
			return redirect(url_for('Login'))
	return wrapper

#首页
@app.route('/')
@Login_required
def index():
	return render_template('index.html')

#定义钩子函数使登陆后的用户显示用户名
@app.context_processor
def My_context_processor():
	user_id = session.get('user_id')
	if user_id:
		user =  User.query.filter(User.id==user_id).first()
		if user:
			return {'user':user}
	return {}


#注销
@Login_required
@app.route('/logout/')
def Logout():
	#删除用户session三种方法
	session.pop('user_id')  #pop  方法删除session
	#del session['user_id']  #del  方法删除session
	#session.clear()               #清除所有session
	return redirect(url_for('Login'))

#登陆
@app.route('/login',methods=['GET','POST'])
def Login():
	if request.method == "GET":
		return render_template('login.html')
	else:
		#获取用户名和密码
		front_username = request.form.get('username')
		front_password = request.form.get('password')
		user = User.query.filter(User.username == front_username,User.password == front_password).first()

		if user:
			session['user_id'] = user.id
			###session.permanent = True      #保流session
			return redirect(url_for('index'))
		else:
			return u"账户名或密码输入错误！"


#注册
@app.route('/regist',methods=['GET','POST'])
def Regist():
	if request.method == 'GET':
		return render_template('regist.html')
	else:
		#获取页面表单内容
		email = request.form.get('email')
		username = request.form.get('username')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')
		#判断用户是否已经存在
		user = User.query.filter(User.username==username).first()

		if user:
			return u"用户已经存在，请更换用户名！"
		else:
			#判断两次输入密码是否一致
			if password1 != password2:
				return u"两次密码输入不一致，请重新输入！"
			else:
				#将用户注册信息写入数据库
				user=User(email=email,username=username,password=password1)
				db.session.add(user)
				db.session.commit()
				#新用户注册成功后跳转到登陆页面
				return redirect(url_for('Login'))

#主机资源
@app.route('/resource/',methods=['GET','POST'])
@Login_required
def Resource ():
	return render_template('resource.html')


@app.route('/add_project/',methods=['GET','POST'])
def Add_project():
	projectname = request.form.get('project_name')
	project_area = request.form.get('project_area')
	project_descriptions = request.form.get('project_descriptions')
	name = Project.query.filter(Project.project_name==projectname).first()
	if name:
		return "项目名称已经存在，请更换项目名"
	else:
		new_project=Project(project_name=projectname,project_area=project_area,project_description=project_descriptions)
		db.session.add(new_project)
		db.session.commit()
		return redirect(url_for('Resource'))



#添加主机
@app.route('/add_host/',methods=['GET','POST'])
def Add_host():
	project_id = request.form.get('select_project')
	hostname = request.form.get('host_name')
	public_add = request.form.get('public_address')
	private_add = request.form.get('private_address')
	os_system = request.form.get('os')
	description = request.form.get('host_descriptions')
	name = Hosts.query.filter(Hosts.host_name==hostname).first()

	if name:
		return "主机已经存在，不能重复添加"
	else:
		HOST_INFO = Hosts(host_name=hostname,public_address=public_add,private_address=private_add,os=os_system,host_description=description)
		HOST_INFO.project=Project.query.filter(Project.id==project_id).first()

		db.session.add(HOST_INFO)
		db.session.commit()
		return redirect(url_for('Resource'))
#显示项目主机
@app.route('/display_host/')
def Display_hosts():
	#根据主机名查找所属的项目
	# name = 'zhongchou_manage'
	# host = Hosts.query.filter(Hosts.host_name==name).first()
	# project_id=host.project_id
	# print(project_id)
	# project= Project.query.filter(Project.id==project_id).first()
	# print(project)
	# return "aaa"
	#使用外键
	# host = Hosts.query.filter(Hosts.host_name == name).first()
	# print(host.project)

	#根据项目查找主机
	projects = Project
	print(projects)
	return "aaaa"



if __name__ == '__main__':
	app.run()
