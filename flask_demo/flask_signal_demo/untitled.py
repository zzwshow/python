from flask import Flask,request,render_template,g,got_request_exception
#from  blinker import Namespace
from signal_demo import login_signal

app = Flask(__name__)

#Namespace 命名空间
# #定义信号
# zlspace = Namespace()
# fire_signal = zlspace.signal("fire")
#
# #监听信号
# def fire_bullet(sender):
#     print(sender)
#     print("start fire bullet")
# fire_signal.connect(fire_bullet)
#
# #发送信号
# fire_signal.send("aaa")

#
# def got_request_error(sender,exception):
#     print(exception)
#
# got_request_exception.connect(got_request_error)



@app.route('/')
def index():
    return render_template("index.html")

@app.route("/login/")
def Login():
    username = request.args.get("username")
    if username:
        g.username = username
        login_signal.send()     #发送信号
        return "用户登录成功"
    else:
        return "用户没有登录"













if __name__ == '__main__':
    app.run(debug=True)
