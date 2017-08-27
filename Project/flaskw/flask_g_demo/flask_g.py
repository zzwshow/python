from flask import Flask,g,request,render_template
from utils import login_log


app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World!'



@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return render_template('login.html')
	else:
		username=request.form['username'] #获取浏览器传过来的用户名！
		password=request.form['password']
		if username == 'admin' and password=='admin':
			#login_log(username)  #通过外部工具方法 记录登陆日志！（第一种方法）
			g.username='admin' #（第二种方法） 将admin 绑定到g.username对象！
			#仅限于本次登陆，在重新登陆或打开其他页面的时候 g.username就会释放掉了！可以理解为暂存区
			login_log() #不需要传参数！外部文件就可以直接调用g.username对象！
			
			
			return u'恭喜登陆成功'
		else:
			return u'用户名或密码错误'
		
		
if __name__ == '__main__':
	app.run()
