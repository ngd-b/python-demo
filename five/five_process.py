#!/usr/bin/python
# -*- coding:utf-8 -*-

# print("hello world")


'''
Pool 进程池，
用于启动多个子进程
'''
from multiprocessing import Pool
import os

# print("current process id:",os.getpid())

def callback(info):
    print("call the fn in process id:",os.getpid())
    print("get args' info:",info)

if __name__ == "__main__":
    childs = Pool(7)
    for index in range(8):
        childs.apply_async(callback,args=(index,))
    print("doing...")
    childs.close()
    childs.join()
    print("ending...")
print("outer ending...")