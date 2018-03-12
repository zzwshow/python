
#定义一个登陆的信号，以后有用户登录进来以后就发送一个登陆信号
#然后就能够监听这个信号，就可以记录当前这个用户登录信息
#用信号的方式，记录用户的登录信息

from blinker import Namespace
from datetime import datetime
from flask import request,g

#定义一个命名空间
namespace = Namespace()
login_signal=namespace.signal("login")


#监听信号  （做些处理）
def login_log(sender):
    #用户名，登录时间，IP地址
    now_time = datetime.now()
    ip = request.remote_addr
    log_line = "{username}*{now_time}*{ip}".format(username=g.username,now_time=now_time,ip=ip)

    with open('login_log.txt','a') as fp:
        fp.write(log_line+"\n")


    print("用户登录了！")
login_signal.connect(login_log)





