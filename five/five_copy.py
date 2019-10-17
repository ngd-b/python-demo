#!/usr/bin/python
# -*- coding:utf-8 -*-

print("hello world")

f = None
try:
    f = open("./hello.txt","r",encoding="utf8")
    print(f.read(5),end='')
    print(f.read(5),end='')
    print(f.read(5))
except IOError as e:
    print(e)
finally:
    if f:
        f.close()

# with auto call the methods' close
with open("./hello.txt","r",encoding="utf8") as f:
    print(f.read())

# readlines() 按行读取文件
with open("./hello.txt","r",encoding="utf8") as f:
    for line in f.readlines():
        print(line.strip())

# 写入数据
with open("./hello_1.txt","w",encoding="utf8") as f:
    f.write("北京欢迎你!")

with open("./hello.txt","a",encoding="utf8") as f:
    f.write("祖国 70!")

# StringIO / BytesIO
from io import StringIO
# 创建
str = StringIO('init')
# 读取初始化进去的值
while True:
    s = str.readline()
    if s == '':
        break
    print(s.strip())
# 写入
str.write("你好!")
str.write(" 南京") 
# 获取
print(str.getvalue())
'''
while True:
    s = str.readline()
    if s == '':
        break
    print(s.strip())
'''
# 写入二进制数据
from io import BytesIO
bi = BytesIO()
bi.write("你好".encode("utf-8"))
print(bi.getvalue())
by = BytesIO(b'\xe4\xbd\xa0\xe5\xa5\xbd')
print(by.read())

# 操作系统文件目录  OS
import os
# 当前环境 nt
print(os.name) 
# python 执行文件    <module 'ntpath' from 'G:\\python-3.7\\lib\\ntpath.py'>
print(os.path)    
# 系统环境配置目录 包括系统环境变量、用户变量、
print(os.environ)      
# 获取当前控制台的管理用户名     'bobol'
print(os.getlogin())
# 创建一个文件、目录
os.mkdir("./foo/") 
# 删除一个目录
os.rmdir("./foo/")

'''
os.path 可以处理部分路径问题
'''
# 获取指定路径的绝对路径     'G:\\pythonDemo\\python-demo\\five'
print(os.path.abspath("./"))
# 返回指定路径是否存在系统文件路径中     False
print(os.path.exists("./foo")) 
# 获取指定路径下文件的大小     4096
print(os.path.getsize("../")) 
# 返回指定路径是否为绝对路径       False
print(os.path.isabs("../"))
