#配置文件
import os
DEBUG = True

SECRET_KEY = os.urandom(24)

###这是公司环境数据库
DIALECT='mysql'
driver='pymysql'
username='root'
password='Cals3615#'
host='10.100.2.105'
port='3306'
database='ops'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,driver,username,password,host,port,database)
SQLALCHEMY_TRACK_MODIFICATIONS=False
