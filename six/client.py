#/usr/bin/python
# -*- coding:utf-8 -*- 

print("hello world")

'''
创建一个客户端程序，连接服务程序

'''
import socket

# 创建
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 进行连接
client.connect(("127.0.0.1",8080))
# 接收服务端的数据
data = client.recv(500)
print("get info: %s" % data.decode("utf-8"))
# 发送一个数据 、 提交一个名称
client.send(b"admin")
# buffer = []
# while True:
#     data = client.recv(500)
#     if data:
#         buffer.append(data)
#     else:
#         break
print("server: %s" % client.recv(500).decode("utf-8"))
# 连接关闭 、发送关闭表示 exit
client.send(b'exit')
# client.close()