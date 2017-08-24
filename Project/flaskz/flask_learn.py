#coding=utf-8
from datetime import datetime
from flask import Flask, render_template #渲染！使用jinja2 模板！
from flask import redirect #连接重定向
from flask import make_response #响应信息
from flask_script import Manager  #管理启动方式
from flask_bootstrap import Bootstrap #增加央视效果
from flask_moment import Moment #指定客户端时间格式 和时区！

#from flask_wtf import Form
 #导入表格类
#from wtforms import StringField,SubmitField #导入字符串字段和提交按钮字段
#from wtforms.validators import required  #导入字段的验证方法required

#class NameForm(Form): #定义一个表单，并继承Form类
	#name=StringField('what is your name?',validators=[required()]) #定义一个name的文本字段。
	#submit=SubmitField('Submit') #定义一个submit的提交按钮！
	
app = Flask(__name__)
manager = Manager(app)  #将应用实例传给Manage()类来管理并赋值给manager
bootstrap=Bootstrap(app)
moment=Moment(app) #初始化程序实例
app.config['SECRET_KEY']='zhang'
#######################################
#定义时间格式！
@app.route('/')
def index():
	return render_template('index.html',
	                       current_time=datetime.utcnow())

#######################################
# @app.route('/')
# def index():
#     return '<h1>Bad Request!</h1>', 404


# @app.route('/baidu') #连接重定向！
# def index():
#     return redirect('https://www.baidu.com')

########################################
# @app.route('/')
# def hello_world():    #创建响应对象！
#     response=make_response('<h1>This document carries a cookie!</h1>') #响应内容！
#     response.set_cookie('answer','42') #设置cookie！
#     return response #返回相应对象！
#
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello %s!</h1>' % name

#######################################
# @app.route('/')  #使用模板
# def index():
#     return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500


if __name__ == '__main__':
	manager.run()
	#调用manager对象的run()方法启动程序
    
