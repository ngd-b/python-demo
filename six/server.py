#/usr/bin/python
# -*- coding:utf8 -*-

print("hellow world")

'''
创建一个server，启动监听 8080 端口，
处理客户端过来的数据请求
'''
import socket 
# 线程控制接口
import threading
# 时间
import time

# AF_INET 指定IPV4 ，SOCK_STREAM 指向面向流的TCP协议
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 指定绑定的IP地址、端口号
server.bind(('127.0.0.1',8080))
# 启动监听 ; 可指定监听连接的最大连接数
server.listen(2)

# 定义处理连接的方法
def handleInfo(sock,addr):
    print("from:%s:%s" % addr)
    sock.send(b"hello!")
    # 等待接收客户端数据
    while True:
        data = sock.recv(500)
        time.sleep(3)
        if not data or data.decode("utf-8")=="exit":
            break
        print("client: %s " % data.decode("utf-8"))
        sock.send(("I get you ! %s" % data.decode("utf-8")).encode("utf-8"))
    sock.close()
    print("the addr %s:%s closed" % addr)
# 处理客户端的连接
while True:
    sock,addr = server.accept()
    # 没过来一个新的连接，创建一个线程来处理
    child = threading.Thread(target=handleInfo,args=(sock,addr))
    child.start()

