from flask import (
	Blueprint,
	views,
	render_template,
	request,session,
	redirect,
	url_for,
	g,
	jsonify
)
from .forms import LoginForm,ResetPwdForm
from .models import CMSUser
from .decorators import Login_Required
from exts import db
from utils import restful
import config


bp = Blueprint("cms",__name__,url_prefix="/cms")  #蓝图url

@bp.route('/')
@Login_Required
def index():
	return render_template("cms/cms_index.html")

#注销
@bp.route('/logout/')
@Login_Required
def logout():
	#session.clear()  #清除所有登录的用户
	del session[config.CMS_USER_ID]
	return redirect(url_for('cms.login'))

#个人中心
@bp.route("/profile/")
@Login_Required
def profile():
	return render_template("cms/cms_profile.html")

##登陆类视图
class LoginView(views.MethodView):

	def get(self,message=None):
		return render_template('cms/cms_login.html',message=message)

	def post(self):
		form = LoginForm(request.form) #验证器获取表单数据
		if form.validate():
			email = form.email.data
			password = form.password.data
			remember = form.password.data
			user = CMSUser.query.filter_by(email=email).first() #验证email 是否存在
			if user and user.check_password(password):
				session[config.CMS_USER_ID] = user.id    #验证成功后添加session 信息！用于以后判断用户是否登陆
				if remember:
					session.permanent = True  #session 过期时间为31天
				return redirect(url_for('cms.index'))  #重定向的蓝图主页（一点要加蓝图名字）

			else:
				return self.get(message="邮箱或密码错误")

		else:
			# message = form.errors.popitem()[1][0] #返回任意一项表单验证器定义的错误提示信息！
			message = form.get_error()   #同上
			return self.get(message=message)

###修改密码类视图
class RestPwdView(views.MethodView):
	decorators = [Login_Required]  #类视图中使用decorators来添加装饰器（限制登录）
	def get(self):
		return render_template('cms/cms_resetpwd.html')

	def post(self):
		form = ResetPwdForm(request.form)
		if form.validate():
			oldpwd = form.oldpwd.data
			newpwd = form.newpwd.data
			user = g.cms_user
			if user.check_password(oldpwd):  #检查旧密码是否正确
				user.password = newpwd
				db.session.commit()
				return restful.success()
			else:
				return restful.parames_error("旧密码错误")

		else:
			# message = form.get_error()   #获取表单验证器的错误提示
			# return jsonify({"code":400,"message":message})
			return restful.parames_error(form.get_error())


####修改邮箱
class ResetEmailView(views.MethodView):
	decorators = [Login_Required]
	def get(self):
		return render_template('cms/cms_resetemail.html')
	def post(self):
		pass






##类视图url 添加到蓝图url中
bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))
###修改密码
bp.add_url_rule('/resetpwd/',view_func=RestPwdView.as_view('resetpwd'))
####修改邮箱
bp.add_url_rule('/resetemail/',view_func=ResetEmailView.as_view('resetemail'))






