from  flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from exts import db
from xmbbs import create_app
from apps.cms import models as cms_models
CMSUser = cms_models.CMSUser

app = create_app()
manager = Manager(app)   #将项目app 加入管理器

Migrate(app,db)          #关联app于db

manager.add_command('db',MigrateCommand)  #将MigrateCommond (包含很多迁移子命令)绑定给db

@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
@manager.option('-e','--email',dest='email')
def create_cms_user(username,password,email):
	user =CMSUser(username=username,password=password,email=email)
	db.session.add(user)
	db.session.commit()
	print("cms 用户添加成功！")

if __name__ == '__main__':
	manager.run()