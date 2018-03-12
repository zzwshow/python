from flask import Flask
from exts import db
import config


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)   #将db 绑定app



@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/profile/')
def Profile():
	pass

if __name__ == '__main__':
	app.run()
