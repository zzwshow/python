from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from exts import db
from ops import app
from models import User,Hosts,Project



#将app加入管理器中
manager = Manager(app)

migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)



if __name__ == '__main__':
	manager.run()
