from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)





@app.route('/')
def hello_world():
	return 'Hello World!'


# db.drop_all()
# db.create_all()


user = User()



if __name__ == '__main__':
	app.run(debug=True,port=3000)
