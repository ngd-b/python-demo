#/usr/bin/pytyon
# -*- coding:utf-8

print("hello world")

'''
UDP 不可靠传输；广播协议 
'''
import socket

# 选择 SOCK_DGRAM UDP类型
us = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
us.bind(("127.0.0.1",8089))

while True:
    data,addr = us.recvfrom(500)
    print(addr)
    print("from: %s:%s get info:" % addr ,data.decode("utf-8") )
    us.sendto(b"I'm coming...",addr)