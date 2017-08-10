#coding=utf-8
import socket
ip_add=('127.0.0.1',8001)

s=socket.socket()
s.connect(ip_add) #链接服务端

while True:
    send_data=input(">>>")
    if send_data == 'exit':break
    if len(send_data) ==0:continue
    s.send(bytes(send_data,encoding='utf-8')) #s.send发送消息

    recv_data=s.recv(1024) #接受服务器发来的消息
    print(str(recv_data,encoding='utf-8'))

s.close() #关闭链接















