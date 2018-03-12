from flask_script import Manager
from flask_restful_demo import app
from flask_migrate import Migrate,MigrateCommand
from exts import db
import models

manager = Manager(app)  #将app绑定给命令管理器
Migrate(app,db)  #将app和db 绑定给迁移工具

manager.add_command('db',MigrateCommand) #将迁移工具绑定给命令管理器




if __name__ == "__main__":
    manager.run()




