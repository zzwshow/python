from flask import Flask
from exts import db   #导入db
import config          #导入配置文件
#from models import Article #导入模型！


app = Flask(__name__)
app.config.from_object(config) #调用外部配置文件
db.init_app(app) #初始化app


#使用了flask_migrate就不需要手动将app加入栈中了
#手动将app推送到栈中！因为flask现在没有执行任何视图函数，app并没有在栈中
#所以db初始化栈中app时找不到app,
# with app.app_context():
#     db.create_all()




@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
