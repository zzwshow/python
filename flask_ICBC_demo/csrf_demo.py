from flask import Flask,render_template,views,request,session
from forms import RegistForm,LoginForm,TransferForm
from exts import db
import config
from models import User
from auth import LoginRequired
from flask_wtf import CSRFProtect


app = Flask(__name__)
app.config.from_object(config)
CSRFProtect(app)
db.init_app(app)


@app.route('/')
def index():
	return render_template('index.html')


class RegistView(views.MethodView):    #注册

	def get(self):
		return render_template("regist.html")

	def post(self):
		form = RegistForm(request.form)
		if form.validate():
			email = form.email.data
			username = form.username.data
			password = form.password.data
			deposit = form.deposit.data
			user = User(email=email,username=username,password=password,deposit=deposit)
			db.session.add(user)
			db.session.commit()
			return "注册成功"

		else:
			print(form.errors)
			return "请输入正确的信息。"


class LoginView(views.MethodView):   #登陆

	def get(self):
		return render_template("login.html")

	def post(self):
		form = LoginForm(request.form)
		if form.validate():
			email = form.email.data
			password = form.password.data
			user = User.query.filter(User.email==email,User.password==password).first()


			if user:
				session['user_id'] = user.id
				return "登陆成功！"

			else:
				return "用户密码或邮箱错误！"


class TransferView(views.MethodView):   #转账

	decorators = [LoginRequired]
	#给类函数增加装饰器，将我们定义的登陆限制装饰器传给decorators 这样下面的（get,post）
	# 都要经过装饰器。

	def get(self):
		return render_template('transfer.html')

	def post(self):
		form = TransferForm(request.form)
		if form.validate():
				#获取要转帐目标的账户信息
			email = form.email.data
			money = form.money.data
			user = User.query.filter_by(email=email).first()

			if user:  #如果目标用户存在，就转账
				#先获取自己的账户信息
				user_id = session.get("user_id")
				myself = User.query.get(user_id)
				if myself.deposit >= money:
					user.deposit += money
					myself.deposit -= money
					db.session.commit()      #提交到数据库
					return "转账成功！"

				else:
					return "余额不组"

			else:
				return "目标用户不存在！"

		else:
			print(form.errors)
			return "数据填写不正确"


#添加url映射
app.add_url_rule("/regist/",view_func=RegistView.as_view('regist'))
app.add_url_rule("/login/",view_func=LoginView.as_view("login"))
app.add_url_rule("/transfer/",view_func=TransferView.as_view("transfer"))


if __name__ == '__main__':
	app.run(debug=True,port=2000)
