from wtforms import Form,StringField,IntegerField,BooleanField
from wtforms.validators import Length,EqualTo,Email,ValidationError,InputRequired,NumberRange


# class Regist_form(Form):
# 	username = StringField(validators=[Length(min=3,max=10,message="用户名长度必须在3到10位之间！")])
# 	password = StringField(validators=[Length(min=6,max=10)])
# 	password_repeat = StringField(validators=[Length(min=6,max=10),EqualTo("password")])

class SettingsForm(Form):
	# email = StringField(validators=[Email()])
	username = StringField("用户：",validators=[InputRequired()])
	age = IntegerField(validators=[NumberRange(10,100)])
	remember = BooleanField("记住我：")
