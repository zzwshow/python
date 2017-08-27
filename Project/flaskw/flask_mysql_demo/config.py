
#连接数据库格式
#mysql+driver://username:password@host:post/database

DIALECT='mysql'
driver='mysqldb'
username='root'
password='Cals998'
host='192.168.10.241'
port='3306'
database='db_demo2'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,driver,username,password,host,port,database)


SQLALCHEMY_TRACK_MODIFICATIONS=False
