from Flask_sqlalchemy_01 import db


HOSTNAME='127.0.0.1'
PORT='3306'
DATABASE='py_demo'
USERNAME='root'
PASSWORD='wei3511'

# dialect+driver://username:password@host:port/database
# DB_URL="mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

DB_URL = "mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8" % (USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)



class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	username = db.Column(db.String(50),nullable=False)






















