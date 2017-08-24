from flask_script import Manager  #导入管理器
from flask_script_demo import app  #导入Manager要应用到的那个实例

#我们把对数据库的操作都放到db_script.py中！导入数据库命令集
from db_script import DBManager

#manager管理实例app
manager=Manager(app)

@manager.command
def runserver():
	print('服务器跑起来了')

#给manager管理器增加自定义的命令！如刚才定义的数据库操作，
# 第一个参数是‘命令标识’
# 第二个参数是上面导入进来的 ‘命令集’
manager.add_command('db',DBManager)




if __name__ == '__main__':
	manager.run()


