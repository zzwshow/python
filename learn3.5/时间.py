#coding=utf-8
import time

print(time.time()) #返回当前系统时间戳
print(time.strftime('%Y-%m-%d-%H:%M:%S')) #返回自定义格式时间字符串

print(time.ctime()) #输出字符串格式时间：Sun Aug 14 16:04:02 2016 ,当前系统时间

print(time.ctime(time.time()-86640))


#----------------------------------------------------
import datetime

print(datetime.date.today()) #获取今天的时间
aa=datetime.date.today() #创建今天的时间对象
aa=str(aa)  #将时间对象转化为字符串
with open(aa,'w+') as ff: #以时间为文件名 ，写入字符串信息
    ff.write('ni hao ')

str_to_date = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M") #将字符串转换成日期格式
new_date = datetime.datetime.now() + datetime.timedelta(days=10) #比现在加10天
new_date = datetime.datetime.now() + datetime.timedelta(days=-10) #比现在减10天
new_date = datetime.datetime.now() + datetime.timedelta(hours=-10) #比现在减10小时
new_date = datetime.datetime.now() + datetime.timedelta(seconds=120) #比现在+120s
print(new_date)

