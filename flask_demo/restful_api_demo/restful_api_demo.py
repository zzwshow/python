from flask import Flask
from flask_restful import Api,Resource,reqparse,inputs

app = Flask(__name__)
api = Api(app)  #将app绑定在Api上

class LoginView(Resource):  #定义一个接口
    def post(self):
        #验证用户名和密码
        parser = reqparse.RequestParser() #定义一个分析请求对象
        parser.add_argument('username',type=str,help="用户名验证错误") #传入要分析的值
        parser.add_argument('password',type=str,help="密码验证错误")
        parser.add_argument('gender',type=str,choise=["male","female","secret"]) #限制客户端提交的数据选项（没有写help粗无信息会提示英文字符）

        parser.add_argument('home_page',type=inputs.url,help="传递的url错误！") #分析post提交的url
        parser.add_argument('telphone',type=inputs.regex(r'1[3578]\d{9}')) #使用正则表达式验证提交的手机号码！

        parser.add_argument('birthday',type=inputs.date,help="生日字段验证错误")

        args = parser.parse_args()  #解析
        print(args)

        return {"username":"zzw"}
api.add_resource(LoginView,'/login/',endpoint='login')  #将接口添加在资源池中！


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
