#!/usr/bin/python
# -*- coding: utf-8 -*-
print("hello world")
name = input("please input your name \n")
print("welcome",name)
# if blocks
if name=="admin":
    print("欢迎管理员登陆!")
else:
    print("登陆成功!")
# 转义
print("hello\nworld")
print(r"hello \n world")
print('''hello
    world''')
# 布尔
print(8>5 and 8<10)
# number
print(2e10)
# ord 对单个字符编码 chr 对单个字符的解码
Name = ord("国")
print(Name)
Name_ = chr(Name)
print(Name_)
print("中国".encode("utf-8"))	

# len 计算字符长度
print(len("hello world"))
# 文本格式化 
print("%d周年" % 70)
print("{0}周年".format(70))
# list 
names = ["花花","小亮","明总"]
print(names[0])
# udpate 
names[0] = 70; 
print(names[0])
# tuple 元组
names_ = (1949,2019,70)
print(names_[2])
# for ... in 循环
for item in names:
	print(item)

# while 循环
num = 3
while num>1:
	print(num*2)
	num = num-1
user = {"袁明":23,"鲁花":32,"祖国":70}
print(user["祖国"])
for key in user.keys():
	print(key,user[key])
# set 只存储值，不重复
age = set([23,32,70,32])
print(age)
# 系统内置函数 , 如 abs() 求绝对值
print(abs(-100))
# 自定义函数
def add(num1,num2):
	return num1+num2

print(add(100,1))

# 返回多个值，类似解构赋值
def add(num1,num2):
    return num1,num2
res1,res2 = add(100,1)
print(res1,res2)
# 函数可变参数
def add(*nums):
    total = 0
    for n in nums:
        total+=n
    return total
print(add(3,4,5,6))
# 函数关键参数，即必须传入的参数和可选参数，
def addUser(name,**other):
    print({"name":name,"other":other})

addUser("祖国",age=70,desc="生日快乐!")
# 参数传入时，可传入 dict , 
info = {"age":70,"desc":"生日快乐!"}
addUser("祖国",**info)
# 命名关键字，即指定可选参数的名称 ,以下 只能传递 'age'属性
def addUser(name,*,age):
	print({"name":name,"other":age})

addUser("祖国",age=70)
# 递归优化
def factorial(n,total):
    if n==1:
        return total
    return factorial(n-1,n*total)
print(factorial(10,total=1))