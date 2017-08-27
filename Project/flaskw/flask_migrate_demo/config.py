
#配置文件

DIALECT='mysql'
driver='mysqldb'
username='root'
password='wei3511'
host='192.168.0.104'
port='3306'
database='db_demo1'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,driver,username,password,host,port,database)


SQLALCHEMY_TRACK_MODIFICATIONS=False
