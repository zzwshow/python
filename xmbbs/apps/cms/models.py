from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

class CMSUser(db.Model):
	__tablename__ = "cms_user"
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	username = db.Column(db.String(50),nullable=False)
	_password = db.Column(db.String(100),nullable=False)
	email = db.Column(db.String(50),nullable=False,unique=True)
	join_time = db.Column(db.DateTime,default=datetime.now)

	def __init__(self,username,password,email):
		self.username = username
		self.password = password
		self.email = email

	#加密password
	@property   #将类中的方法变为类的属性！外部使用CMSUser.password来获取密码
	def password(self):
		return self._password

	# 上面已经把password变为了属性，我们就可以给属性赋值，CMSUser.password="abc123"
	# @password.setter装饰器可以在复值时给他进行一些处理，如加密
	@password.setter
	def password(self,raw_password):
		#加密密码
		self._password = generate_password_hash(raw_password)

	def check_password(self,raw_password):
		#验证密码
		result = check_password_hash(self.password,raw_password)
		return result




