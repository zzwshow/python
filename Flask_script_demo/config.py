###这是公司PC环境数据库

username='root'
password='wei3511'
host='127.0.0.1'
port='3306'
database='flask_migrate_demo'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (username,password,host,port,database)

SQLALCHEMY_DATABASE_URI = DB_URI
