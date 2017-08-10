#函数式编程，编程规范：
#以后写函数按照下面这个例子来编写,规范,这是一个登录注册的函数编程
# 1.函数与函数间隔2行
#
# 2.函数需要注释,便于记忆
#
# 3.函数名需要见名知意

#db格式
# admin|12345
# user1|22222

#定义一个验证函数
def login(username,password):
    """
    :param username: 用户输入的用户名
    :param password: 用户输入的密码
    :return: 返回值：true表示成功，false 表示失败
    """
    f=open('db','r')
    for line in f:
        line_list = line.strip().split('|')
        if line_list[0] == username and line_list[1] == password:
            return True

    return False

#定义一个注册函数
def register(username,password):
    f= open('db','a')
    tmp = '\n'+username+'|'+password
    f.write(tmp)
    f.close()
    print("恭喜你已经注册成功")

#定义用户选项

def main():
    t=input("请输入选项：debark（登陆）||reg（注册）>>>:")
    if t == "debark":
        name=input('Please input user name:')
        pa=input('Please input user password:')
        r=login(name,pa)
        if r:
            print("登陆成功")
        else:
            print("登陆失败")
    elif t == "reg":
        name = input('Please input user name:')
        pa = input('Please input user password:')
        register(name,pa)
    else:
        print("你输入错误选项")


main()



























