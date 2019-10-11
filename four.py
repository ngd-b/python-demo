#!/usr/bin/python
# -*- coding:utf-8 -*-

print("hello world")

# print(a)
try:
    print(a)
except NameError as e:
    print("变量未声明，请检查")
finally:
    print("继续执行!")
print(2)

# logging 记录日志
import logging
try:
    print(10/0)
except ZeroDivisionError as e:
    logging.exception(e)

print(0/10)

# 自定义错误类型
class ConflictValueError(ValueError):
    pass

name = input("please input your name \n")
try:
    if name == "admin":
        raise ConflictValueError("you can't use this name")
except ConflictValueError as e:
    logging.exception(e)

print("ok")

# 断言
import pdb
assert name!="test","测试"
pdb.set_trace()
print("大神，你好")