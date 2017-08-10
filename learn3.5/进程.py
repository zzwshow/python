#coding=utf-8

# import os
#
# print('I am child process (%s) start....'%os.getpid())
#
# pid=os.fork()
#
# if pid==0:
#     print('I am child process (%s) and my parent is %s' %(os.getpid(),os.getppid()))
#
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(),pid))

#windowns 上没有fork()功能 以上代码只能在linux上运行！
#answer
# Process (876) start...
# I (876) just created a child process (877).
# I am child process (877) and my parent is 876.

#----------------------------------------------------------------
#
# from multiprocessing import Process   #导入进程模块
# import os  #导入os模块
#
# #子进程要执行的代码
# def run_proc(name):   #定义一个函数
#     print('Run child proess %s (%s)' % (name,os.getpid()))
#
# if __name__ == '__main__':
#     print('Parent process is %s ' % os.getpid()) #本脚本运行启动为主进程！
#
#     p = Process(target=run_proc,args=('test',))  #创建一个子进程对象！子进程运行目标为上面的函数
#                                                 #函数的参数为‘test’
#     print('Child process will start')
#     p.start()                                #启动子进程
#     p.join()                        #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
#     print('Child process end')
#

#------------------------------------------------------------------------
#Pool
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)'% (name,os.getpid()))
    start=time.time()
    time.sleep(random.random())
    end=time.time()
    print('Task %s runs %0.2f seconds.'% (name,(end-start)))


if __name__ == '__main__':
    print('Parent process is %s'% os.getpid()) #打印父进程ID
    p =Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))

    print('Waiting for all subprocesses done!!!')
    p.close()
    p.join()
    print('all subprocess done....')





















