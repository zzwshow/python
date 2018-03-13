DEBUG = True
import os

SECRET_KEY = os.urandom(24)

###数据库

# DB_URI = "mysql+pymysql://root:wei3511@127.0.0.1:3306/xmbbs_db?charset=utf8"

DB_URI = "mysql+pymysql://root:wei3511@127.0.0.1:3306/xmbbs_db1?charset=utf8"

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False

#临时定义session 变量
CMS_USER_ID = "aaaa"