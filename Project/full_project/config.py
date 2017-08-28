import os

#调试配置
debug=True
#session加密
SECRET_KEY=os.urandom(24)

###这是家里环境数据库
# DIALECT='mysql'
# driver='mysqldb'
# username='root'
# password='wei3511'
# host='192.168.0.104'
# port='3306'
# database='full_pro'
#
# SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,driver,username,password,host,port,database)
#
# SQLALCHEMY_TRACK_MODIFICATIONS=False
#######################################################
###这是公司环境数据库
DIALECT='mysql'
driver='mysqldb'
username='root'
password='Cals998'
host='192.168.10.241'
port='3306'
database='full_pro'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,driver,username,password,host,port,database)
SQLALCHEMY_TRACK_MODIFICATIONS=False