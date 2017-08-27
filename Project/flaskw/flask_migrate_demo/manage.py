from flask_script import Manager #导入管理工具
from  flask_migrate_demo import app #从主程序导入app实例
from flask_migrate import Migrate,MigrateCommand
from exts import db
from models import Article #将要迁移的模型导入进来！

#管理器绑定主程序实例app 用于管理app
manager=Manager(app)

#1\使用flask_migrate，必须绑定app和db
migrate = Migrate(app,db)

#2\把MigrateCommand命令添加到管理器manager对象中
manager.add_command('db',MigrateCommand)



if __name__ == '__main__':
    manager.run()

