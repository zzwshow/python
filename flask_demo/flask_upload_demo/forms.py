from wtforms import Form,StringField,FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired,FileAllowed
#FileRequired :必须传入文件
#FileAllowed ：允许那些文件上传

#定义表单验证器
class Uploadform(Form):
    avatar = FileField(validators=[FileRequired(),FileAllowed(["png","jpg","gif"])])
    desc = StringField(validators=[InputRequired()])
