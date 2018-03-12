from exts import db

#定义三个模型
#1、用户模型
#2、文章模型
#3、标签模型

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))


#article  和 tag 是多对多的关系，所有要定义一个中间表，用来关联
article_tag_table = db.Table('article_tag',
            db.Column('article_id',db.Integer,db.ForeignKey("article.id"),primary_key=True),
            db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key=True)
)

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    #article 与user表为一对多，这里应用外键

    #根据文章找作者，反转后是根据作者找到所有文章
    author = db.relationship('User',backref="articles")  #定义反转
    #根据文章找到所属的标签，反转是根据标签找到标签下的所有文章
    tags = db.relationship("Tag",secondary=article_tag_table,backref="tags")


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))











