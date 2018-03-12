from flask_script import  Manager
from Flask_demo import app
from exts import db
from flask_migrate import Migrate,MigrateCommand
from models import User   #将要映射到数据库的模型导入进来   不然不会映射到数据库中！

#Migrate  用来绑定app和db的
#MigrateCommand 包含很多子命令  实际上底层是基于alembic

manager = Manager(app)  #将项目绑定到管理器中
#先将app和db 绑定到Migrate 中！
Migrate(app,db)

#使用flask_script  将MigrateCommand 下的子命令绑定到 “db” 上方便使用
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
	manager.run()



