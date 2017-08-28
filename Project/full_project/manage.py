#命令集文件
from flask_script import Manager #导入实例管理器
#（flask_migrate）数据库迁移工具（可以在不删表的情况下更新数据库字段！）
from flask_migrate import MigrateCommand,Migrate
from exts import db #（flask_migrate)需要用到
from full_project import app #将主程序实例导入进来，绑定给管理器！
from models import User #导入数据库模型！




#将实例绑定给管理器并赋值给对象manager
manager=Manager(app)

#使用Migrate绑定app和db
migrate=Migrate(app,db)

#添加迁移脚本的命令到manager管理器中
manager.add_command('db',MigrateCommand)




if __name__ == '__main__':
    manager.run()

