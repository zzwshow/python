from flask_script import Manager #导入管理器
#因为这个文件不是主文件，不需要传入实例
DBManager=Manager()

@DBManager.command
def init():
	print('数据库初始化成功')
	

@DBManager.command
def migrate():
	print('数据库迁移成功')
	

