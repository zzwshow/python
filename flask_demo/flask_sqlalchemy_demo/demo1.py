from sqlalchemy import create_engine,Column,Integer,Float,Boolean,DateTime,String,func,Text,and_,or_,ForeignKey
from sqlalchemy.ext.declarative import declarative_base   #用来生成模型基类
from sqlalchemy.orm import sessionmaker,relationship,backref  #用于生成数据库会话对象


HOSTNAME='127.0.0.1'
PORT='3306'
DATABASE='py_demo'
USERNAME='root'
PASSWORD='wei3511'

# dialect+driver://username:password@host:port/database
DB_URL="mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)
#创建连接引擎
engine=create_engine(DB_URL)

#声名一个数据库引擎得元类  （供模型类继承）
Base = declarative_base(engine)

#定义数据库会话对象！用于增删改查
session = sessionmaker(engine)()

#父表/子表
# user/article

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer,primary_key=Text,autoincrement=True)
	username = Column(String(50),nullable=False)

	#articles = relationship("Article") #定义关系  查找用户所发表的所有文章

	def __repr__(self):
		return "User(usernmae:%s)" % self.username

class Article(Base):
	__tablename__ = 'article'
	id = Column(Integer,primary_key=True,autoincrement=True)
	title = Column(String(50),nullable=False)
	content = Column(Text,nullable=False)

	uid = Column(Integer,ForeignKey('user.id'))   #外键
	autor = relationship("User",backref='articles')


	def __repr__(self):
		return "Article(title:%s,content:%s)" % (self.title,self.content)


Base.metadata.drop_all()
Base.metadata.create_all()


user = User(username='zzw')

article1 = Article(title='abc1',content='123')
article2 = Article(title='abc2',content='yyyy')

user.articles.append(article1)
user.articles.append(article2)

session.add(user)
session.commit()


























