from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import  config

app = Flask(__name__)
app.config.from_object(config)
db=SQLAlchemy(app)


class User(db.Model):
	__tablename__ = 'users'
	id=db.Column(db.Integer,primary_key=True,autoincrement=True)
	username=db.Column(db.String(100),nullable=False)

class Article(db.Model):
	__tablename__ = 'article'
	id=db.Column(db.Integer,primary_key=True,autoincrement=True)
	title=db.Column(db.String(100),nullable=False)
	content=db.Column(db.Text, nullable=False)
	author_id=db.Column(db.Integer,db.ForeignKey('users.id'))
	
	author=db.relationship('User',backref=db.backref('articles'))

db.create_all()

@app.route('/')
def index():

	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True,port=1000)
	

