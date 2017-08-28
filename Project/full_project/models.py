#存放数据库模型！
from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    telephone=db.Column(db.String(11),nullable=False)
    username=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(100),nullable=False )


class Question(db.Model):
    __tablename__='question'
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    title=db.Column(db.String(100),nullable=False)
    content=db.Column(db.Text,nullable=False)
    #now()获取的事服务器第一次运行的时间
    #now就是每次创建一个模型的当前时间！
    create_time=db.Column(db.DateTime,default=datetime.now)
    author_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    author=db.relationship('User',backref=db.backref('questions'))
    
    
    
    