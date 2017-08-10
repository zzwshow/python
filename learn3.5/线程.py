#coding=utf-8
#创建线程的方式

#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行



import threading
import time

# def f1(arg):
#     time.sleep(0.1)
#     print(arg,threading.current_thread().name)
#
# for i in range(10):
#     t=threading.Thread(target=f1,name='thread---',args=('python',))
#     #创建线程对象！执行函数并传入参数‘python’,name='thread---' 设置线程名称！
#     t.start() #线程对象调用start()函数，启动线程！
#
#     print(t.getName()) #打印线程名称！

#############################################

def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n +=1
        print('thread %s >>>' % threading.current_thread().name,n)
        time.sleep(1)
    print('thread %s is ended!!!!' % threading.current_thread().name)

if __name__ == '__main__':
    print('thread %s is running...' % threading.current_thread().name) #打印现在线程名！主线程（mainthread）
    t=threading.Thread(target=loop,name='childhread') # 创建子线程实例，并设置子线程名字
    t.start()                                       #启动线程
    t.join()                                        #等待子线程运行完之后在向下执行！
    print('thread  %s  ended!!!' % threading.current_thread().name)

#执行结果如下
# thread MainThread is running...
# Thread childhread is running...
# thread childhread >>> 1
# thread childhread >>> 2
# thread childhread >>> 3
# thread childhread >>> 4
# thread childhread >>> 5
# thread childhread is ended!!!!
# thread  MainThread  ended!!!

#-----------------------------lock
# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，
# 互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。










