#coding=utf-8

try:
    try:
        raise IOError   #返回给上以及的是IOError
    except IOError:     #捕获到IOError异常
        print("inner exception!!!")
        raise           #在次将IOError抛出到上层
except IOError:         #再次捕获异常
    print('outter exception!!!')















