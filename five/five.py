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
with open("./hello.txt","w",encoding="utf8") as f:
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