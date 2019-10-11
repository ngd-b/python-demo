#!/usr/bin/python
# -*- coding:utf-8 -*-

print("hello world")

# pthon 中的关键字
import keyword
print(keyword.kwlist)

# 注释
'''
一行注释
二行注释
'''
"""
三行注释
四行注释
"""
print("多行注释")

# 单行语句换行
print("you"
    "are"
    "my"
    "friend")
# 这种运算则需要使用 \ 符
count = 23+ \
    12+ \
    34 
print(count)

# 字符串 复用
print("祖国"*2)

# print() 不换行
print("祖国",end="")
print("70")

# 变量赋值
a = b = c = 20
b = 30
print(a,b,c)
a,b,c = 32,32,44
print(a,b,c)