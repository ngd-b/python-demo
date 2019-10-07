#!/usr/bin/python
# --*-- coding:utf-8 --*--
print("hello world")

# [:]
names = list(range(11))
print(names[1:6])
# [::]
print(names[1:6:2])
# 判断当前数据是否可以进行迭代
from collections.abc import Iterable
print(isinstance(names,Iterable))

# enumerate
names = enumerate(names)
for k,v in names:
    print(k,v)

# []
nums = [n*n for n in [2,4,8]]
print(nums)
# 多层操作
nums = [n*m for n in [2,4,8] for m in [1,3,6]]
print(nums)
# generator
names=(n*n for n in [2,4,8])
for val in names:
    print("for-",val)
# print(next(names))

# 判断当前数据类型是否为迭代对象
from collections.abc import Iterator
print(isinstance(nums,Iterator))
print(isinstance(names,Iterator))
print(isinstance(iter(nums),Iterator))

# 匿名函数
total = lambda val:val*3
print(total(4),total.__name__)


# 装饰器 @
def log(fn):
    def wrapper(*arg,**oth):
        print("------操作--------",fn.__name__,"---------操作用户名称---------",arg[0])
        return fn(*arg,**oth)
    return wrapper

@log
def login(user):
    print("欢迎登陆:"+user)


login("admin")
# 装饰器传入自定义参数 
import functools
def log(bool):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*arg,**oth):
            print("------操作--------",fn.__name__,"---------操作用户名称---------",arg[0])
            if bool:
                print("2019-10-06")
            return fn(*arg,**oth)
        return wrapper
    return decorator
@log(True)
def login(user):
    print("欢迎登陆:"+user)

login("test")

# 设定函数默认值
def info(name,flag = True):
    adorn = ""
    if flag:
        adorn = "尊贵的"
    print("欢迎"+adorn+"客人:",name)

info("admin",False)
info("test",False)
# 通过 functools.partial() 设置处理
info_ = functools.partial(info,flag=False)
info_("admin")
info_("test")

# 模块使用
from logs.info import print_log
import user.info

print_log()
print(user.info._Author_)

# re 模块 正则表达式
import re

print(re.match(r".+lo","hello"))
print(re.split(r"l+","hello"))

# groups         ('h', 'lo')
print(re.match(r"^([a-z]+)el([a-z]+)$","hello").groups())
# 对表达式及进行编译，
reg_ = re.compile(r"(\d+)\+(\d+)");
print(reg_.match("2233+123").group(1))