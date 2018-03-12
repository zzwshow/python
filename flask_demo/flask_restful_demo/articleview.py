from flask import Blueprint
from flask_restful import Api,Resource,fields,marshal_with
from models import Article

#在蓝图中使用，restful-api


article_bp = Blueprint('article',__name__,url_prefix='/article')
api = Api(article_bp)   #将蓝图的url传递给flask-restful.Api中！

#定义一个获取文章的接口
class ArticleView(Resource):
    resource_fields = {     #定义要返回给前端的字段！
        'article_title':fields.String(attribute='title'), #修改返回给前端的key名，然后artribut来指明这个是归属article.title字段！
        'content':fields.String,
        'author':fields.Nested({
            #author,需要用嵌套Nested来取出信息，因为article.author对应的是User数据库模型，
            # 必须使用article.author.username 才能获取真正的用户名信息！
            'username':fields.String,
            'email':fields.String
        }),
        'tags':fields.List(fields.Nested({  #同上，因为它返回的是一个列表所以先有个列表字段，在嵌套相应的数据信息，！
            'id':fields.String,
            'name':fields.String
        })),
        'read_count':fields.Integer(default=80)
        #在article模型中没有这个read_count字段，这里可以定义一个默认返回阅读数为80的字段，
        # 就是模型中没有的字段，这里可以曾添字段返回给前端！
    }

    # 绑定resoutce_fields，就会从article中取出resource_fields中包含的字段然后返回给客户端！article中没有的话就会返回None
    @marshal_with(resource_fields)
    def get(self,article_id):
        article = Article.query.get(article_id) #根据用户提交的article_id 获取文章
        return article


#将接口添加到api-----url资源池中！(从URL中获取用户要查询的article_id)
api.add_resource(ArticleView,'/<article_id>/',endpoint='article')

#注意:
    # 现在接口地址为：http://127.0.0.1/article/1/     (它是蓝图的url_prefix前缀，加上api---url资源池的url路径组合)
