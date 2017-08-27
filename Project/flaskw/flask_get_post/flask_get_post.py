from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/search/')
def search():
	#获取get请求传进来的参数（传进来的参数是字典格式）
	q= request.args.get('q')

	return u'用户提交的查询参数是：%s' % q

@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.form['username']
		password = request.form['password']
		return username,password



if __name__ == '__main__':
	app.run(debug=True,port=200)
	
