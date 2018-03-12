from wtforms import StringField,FloatField,Form
from wtforms.validators import Email,Length,EqualTo,InputRequired,NumberRange
from models import User

class RegistForm(Form):
	email = StringField(validators=[Email()])
	username = StringField(validators=[Length(min=3,max=20)])
	password = StringField(validators=[Length(min=6,max=20)])
	password_repeat = StringField(validators=[Length(min=3,max=20),EqualTo("password")])
	deposit = FloatField(validators=[InputRequired()])

class LoginForm(Form):
	email = StringField(validators=[Email()])
	password = StringField(validators=[Length(min=6, max=20)])


	# def validate(self):
	# 	result = super(LoginForm, self).validate()
	# 	if not result:
	# 		return False
	# 	email = self.email.data
	# 	password = self.password.data
	#
	# 	user = User.query.filter(User.email==email,User.password==password)
	# 	if not user:
	# 		self.email.errors.append("邮箱或密码不正确。")
	# 		return False
	# 	return True

class TransferForm(Form):
	email = StringField(validators=[Email()])
	money = FloatField(validators=[NumberRange(min=1,max=1000000)])

















