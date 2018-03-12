from flask import Blueprint,views,render_template,request,session,redirect,url_for
from .forms import LoginForm
from .models import CMSUser
from .decorators import Login_Required
import config


bp = Blueprint("cms",__name__,url_prefix="/cms")  #蓝图url

@bp.route('/')
@Login_Required
def index():
	return "cms index"

#登陆类视图
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
			message = form.errors.popitem()[1][0] #返回任意一项表单验证器定义的错误提示信息！
			return self.get(message=message)

#类视图url 添加到蓝图url中
bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))


