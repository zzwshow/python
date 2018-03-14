from wtforms import StringField,IntegerField
from wtforms.validators import Email,InputRequired,Length,EqualTo
from ..forms import BaseForm  #

#登陆表单验证
class LoginForm(BaseForm):
	email = StringField(validators=[Email(message="请输入正确的邮箱格式！"),InputRequired(message="请输入邮箱！")])
	password = StringField(validators=[Length(4,20,message="请输入正确的密码！")])
	remember = IntegerField()


#修改密码表单验证
class ResetPwdForm(BaseForm):
	oldpwd = StringField(validators=[Length(4,20,message="旧密码-格式错误！")])
	newpwd = StringField(validators=[Length(4,20,message="新密码-格式错误！")])
	newpwd2 = StringField(validators=[EqualTo("newpwd",message="两次密码不一致！")])

