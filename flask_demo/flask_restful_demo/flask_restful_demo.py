from flask import Flask
from exts import db
import config
from models import User,Article,Tag
from articleview import article_bp


app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(article_bp)  #将蓝图注册给这个app项目
db.init_app(app)


@app.route('/')
def hello_world():
    #定义一个用户和一篇文章，并将这个用户绑定为这片文章的作者
    user = User(username='zhangzhiwei',email="wei3511@126.com")
    article =Article(title='abc',content='123')
    article.author = user

    tag1=Tag(name="前端")   #定义两个标签
    tag2=Tag(name="python")
    article.tags.append(tag1)   #将两个标签绑定给这个article
    article.tags.append(tag2)

    db.session.add(article)  #提交到数据库中
    db.session.commit()


    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True,port=3000)
