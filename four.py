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
# assert name!="test","测试"
# pdb.set_trace()
print("大神，你好")

# 自定义表单校验错误类
class ExistError(ValueError):
    pass

class PureNumberError(ValueError):
    pass

class LenError(ValueError):
    pass
# 表单用户名校验 、 不能是纯数字、不能有特殊符号、必须6位以上
import re
class ValidForm():
    def __init__(self,**ot):
        self.form = ot
    def exist_name(self):
        form = self.form
        if "name" in form:
            pass
        else:
            raise ExistError("必须填写用户名!") 
    def conflict_name(self):
        form = self.form
        self.exist_name()
        if form["name"] in ["admin","test","login"]:
            raise ConflictValueError("你不能使用这个名字")
    def pureNumber_name(self):
        form = self.form
        self.conflict_name()
        if re.search(r'^\d+$',str(form["name"]))!=None:
            raise PureNumberError("不能是纯数字!")
    def len_name(self):
        form = self.form
        self.pureNumber_name()
        if len(form["name"]) < 4:
            raise LenError("用户名不少于4个字符!")
    def isAvailable(self):
        self.len_name()
        return True

# ValidForm(**{"name":"232"}).isAvailable()
