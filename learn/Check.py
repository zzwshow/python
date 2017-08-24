#coding=utf-8

import os,sys
import time
import pycurl
URL=sys.argv[1]
print(URL)
#URL=str(URL[0])
#URL="https://www.hybjf.com"

c = pycurl.Curl()
c.setopt(pycurl.URL,URL)
c.setopt(pycurl.CONNECTTIMEOUT,5)
c.setopt(pycurl.TIMEOUT,5)
c.setopt(pycurl.NOPROGRESS,1)
c.setopt(pycurl.FORBID_REUSE,1)
c.setopt(pycurl.MAXREDIRS,1)
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
indexfile=open(os.path.dirname(os.path.realpath(__file__))+"\\content.txt",'wb')
c.setopt(pycurl.WRITEHEADER,indexfile)
c.setopt(pycurl.WRITEDATA,indexfile)

try:
    c.perform() #提交请求
except Exception as e:
    print("connecion error" + str(e))
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME=c.getinfo(c.NAMELOOKUP_TIME)  #获取DNS解析时间
CONNECT_TIME = c.getinfo(c.CONNECT_TIME) #获取建立链接的时间
PRETRANSFER_TIME=c.getinfo(c.PRETRANSFER_TIME)#获取从建立链接到准备传输所消耗的时间
STARANSFER_TIME=c.getinfo(c.STARTTRANSFER_TIME) #获取从建立链接到传输开始消耗的时间
TOTAL_TIME=c.getinfo(c.TOTAL_TIME)    #获取传输的总时间
HTTP_CODE=c.getinfo(c.HTTP_CODE)         #获取http状态码
SIZE_DOWNLOAD=c.getinfo(c.SIZE_DOWNLOAD) #获取下载数据
HEADER_SIZE=c.getinfo(c.HEADER_SIZE)      #获取HTTP头部大小
SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD) #获取平均下载速度

print('HTTP状态码：%s' % HTTP_CODE)
print('DNS解析时间：%.2f ms' % NAMELOOKUP_TIME)
print('建立链接时间：%.2f ms' % CONNECT_TIME)
print('准备传输时间：%.2f ms' % PRETRANSFER_TIME)
print('传输开始时间：%.2f ms' % STARANSFER_TIME)
print('传输结束时间：%.2f ms '%TOTAL_TIME)
print('下载数据包大小：%d bytes/s' % SIZE_DOWNLOAD)
print('HTTP头部大小：%d byte' % HEADER_SIZE)
print('平均下载速度：%d byte/s' % SPEED_DOWNLOAD)

indexfile.close()
c.close()













