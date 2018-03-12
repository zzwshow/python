from flask import Blueprint,views,render_template

bp = Blueprint("cms",__name__,url_prefix="/cms")  #蓝图url

@bp.route('/')
def index():
	return "cms index"

#登陆类视图
class LoginView(views.MethodView):

	def get(self):
		return render_template('cms/cms_login.html')

	def post(self):
		pass


#类视图url 添加到蓝图url中
bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))


