###这是家里环境数据库
username='root'
password='wei3511'
host='127.0.0.1'
port='3306'
database='flask_restful_demo'

SQLALCHEMY_DATABASE_URI="mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(username,password,host,port,database)


SQLALCHEMY_TRACK_MODIFICATIONS=False
