from flask import Flask,render_template,request,redirect,url_for,session
import config #导入配置信息
from models import User #导入模型（用于查询手机号）
from exts import db  #导入数据库连接对象！（用于插入数据库数据）
from datetime import timedelta #日期时间间隔对象（设置session过期时间）


#主程序
app = Flask(__name__)
app.config.from_object(config) #实例调用配置文件
db.init_app(app) #初始化(app)
app.config['PERMANENT_SESSION_LIFETINE'] = timedelta(days=7)



##前端框架是用bootstrap
@app.route('/')
def index():
    return render_template('index.html')

##登录页面路由
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        #登录验证，首先拿到用户输入表单中的数据！
        telephone=request.form.get('username')
        password=request.form.get('password')
        #从数据库中查找用户的输入是否存在（验证用户手机号和密码）
        user=User.query.filter(User.telephone==telephone,User.password==password).first()

        if user:
            # 将登录用户的id 放入session中！记录用户登录状态！
            session['user_id']=user.id
            #设置session保留7天
            session.permanent=True
            #登录成功之后页面跳转到首页
            return redirect(url_for('index'))
        else:
            return u'手机号或密码输入错误，请确认后重新登陆...'


##注册页面
@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #1、判断手机号是否存在。如果存在就不让注册了
        user = User.query.filter(User.telephone==telephone).first()
        if user:
            return u'改手机号码已经注册，请更换手机号码...'
        else:
            # 2、判断用户两次输入密码是否一致
            if password1 != password2:
                return u'两次输入密码不一致...'
            else:
                user=User(telephone=telephone,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                #如果注册成功，页面跳转到登录页面！
                return redirect(url_for('login'))



if __name__ == '__main__':
    app.run()


















