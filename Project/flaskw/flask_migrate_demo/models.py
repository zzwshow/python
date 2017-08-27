
from  exts import db

class Article(db.Model):
    __tablename__='article'
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    title=db.Column(db.String(100),nullable=False)
    # content = db.Column(db.Text,nullable=False)



#因为app.create_all()在后期修改字段的时候不会自动映射到数据库中，
#必须删除原来的数据库，重新执行app.create_all()，显然不符合要求
#所以才用flask-migrate可以在每次修改数据库模型字段后自动映射到数据库中！
#需要安装flask-migrate
#使用flask-script 新建manage文件

