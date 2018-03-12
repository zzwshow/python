from exts import db

class User(db.Model):
	__tablename__ = "users"
	id=db.Column(db.Integer,primary_key=True,autoincrement=True)
	email=db.Column(db.String(20),nullable=False)
	username=db.Column(db.String(50),nullable=False)
	password=db.Column(db.String(100),nullable=False)

class Project(db.Model):
	__tablename__ = 'project'
	id=db.Column(db.Integer,primary_key=True,autoincrement=True)
	project_name = db.Column(db.String(50),nullable=False)
	project_area = db.Column(db.String(50),nullable=False)
	project_description = db.Column(db.Text,nullable=False)

class Hosts(db.Model):
	__tablename__ = "hosts"
	id=db.Column(db.Integer,primary_key=True,autoincrement=True)
	host_name=db.Column(db.String(100),nullable=False)
	public_address=db.Column(db.String(100),nullable=False)
	private_address=db.Column(db.String(100),nullable=False)
	os = db.Column(db.String(50),nullable=False)
	host_description = db.Column(db.Text, nullable=False)
	project_id = db.Column(db.Integer,db.ForeignKey('project.id'))  #定义外键
	#知道主机查找主机属于那个项目           #定义反转根据项目查找项目下的所有主机
	project=db.relationship('Project',backref=db.backref('all_host'))


