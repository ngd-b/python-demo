#/usr/bin/python
# -*- coding:utf-8 -*- 

print("hello world")

'''
创建一个客户端程序，连接服务程序

'''
import socket

# 创建
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 发送一个数据 、 提交一个名称
client.sendto(b"admin",("127.0.0.1",8089))
print("server: %s" % client.recv(500).decode("utf-8"))
# client.close()