
from  exts import db

class Article(db.Model):
    __tablename__='article'
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    title=db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)

# class Alembic(db.Model):
#     __tablename__ = "alembic_version"
#     version_num = db.Column(db.String(32),primary_key=True,nullable=False)
#
#     @staticmethod
#     def clear_A():
#         for i in Alembic.query.all():
#             print(i.version_num)
#             db.session.delete(a)
#             db.session.commit()
#         print('==== data in table:Alembic cleared!')

#因为app.create_all()在后期修改字段的时候不会自动映射到数据库中，
#必须删除原来的数据库，重新执行app.create_all()，显然不符合要求
#所以才用flask-migrate可以在每次修改数据库模型字段后自动映射到数据库中！
#需要安装flask-migrate
#使用flask-script 新建manage文件



#运行方法！
#1、进入虚拟环境， 初始化一个迁移的环境: python manage.py db init
#2、将模型生成迁移文件：python manage.py db migrate
#3、将迁移文件映射到数据库中去：python manage.py db upgrade


#如果新添加了字段（只需要执行2-3步骤）