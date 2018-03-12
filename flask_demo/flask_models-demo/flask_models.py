from flask import Flask

#分开models和解决循环引用！
app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World!'


if __name__ == '__main__':
	app.run()
