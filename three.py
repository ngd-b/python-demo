#!/usr/bin/python
# -*- coding:utf-8 -*-
print("hello world")

# 类与实例， class
class User():
    # 类属性
    __Name__  = "User"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        print(self.name)

    def getAge(self):
        print("you won't get the age")

Ming = User("ming",32)
#Ming.getName()
#Ming.getAge()
#print(Ming.age)
print(Ming.__Name__)
# 封装
class User(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        self.__name__ = name

    def getName(self):
        print(self.__name)

    def getAge(self):
        print("you won't get the age")

Ming = User("ming",32)
Ming.getName()
Ming.getAge()
#print(Ming.__name)
print(Ming.__name__)
Ming.__name = "ming_copy"
Ming.getName()
print(Ming.__name)

# 继承、多态
class People():
    def eat(self):
        print("eat meat")
class User(People):
    def walk(self):
        print("walking...")

class Young(People):
    def study(self):
        print("studying...")

class Child():
    def cry(self):
        print("crying...")

    def eat(self):
        print("eat milk")

p_1 = User()
p_2 = Young()
p_3 = Child()

p_3.eat()
p_2.eat()
p_1.walk()

# 对象属性的操作
print(type(None))

import types

print(type(User.eat)==types.FunctionType)
print(type(abs))

print(isinstance(p_1,People))
print(isinstance(p_1,User))

print(dir(p_1))
# 获取一个实例对象的方法，并调用
getattr(p_1,"eat")()
print(hasattr(p_1,"name"))
# 设置一个实例对象的额外的参数
setattr(p_1,"name","peope_one")
print(hasattr(p_1,"name"))

# 高级特性 、类操作说明
class People():
    __slots__ = ('name','age')
    def eat(self):
        print("eat meat")
class User(People):
    # __slots__ = ()
    def walk(self):
        print("walking...")

p = People()
p.name = "people"
# p.address = "address"
print(dir(p))

p_1 = User()
p_1.address = "001"
print(dir(p_1))

# @property 定义并转换为动态添加的属性提供方法，并进行属性处理
class People():
    __slots__ = ('age')
    def eat(self):
        print("eat meat")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,val):
        if val=="admin":
            raise ValueError("you can't use the name")
        self._name = val

people = People()
# people.name = "admin"

# 多重继承
class Boy(User,Young):
    pass

# Boy 拥有了 study  walk  两个技能
print(dir(Boy))

# 特殊形式表达
class Boy(User,Young):
    def __len__(self):
        return 100
# __len__
print(len(Boy()))

class Boy(User,Young):
    def __str__(self):
        return "the object inherit <User>.<Young>"
    __repr__ = __str__
# __len__
print(Boy())

import random
class Boy():
    def __iter__(self):
        return self

    def __next__(self):
        age = random.randint(0,100)
        if age>90:
            raise StopIteration()
        return age

b_age = Boy()
for val in b_age:
    print(val)

class Boy():
    def __getitem__(self,index):
        return index*2

print(Boy()[4])


# print(Boy()())
print(callable(Boy()))
class Boy():
    def __call__(self):
        print("olololololo")
Boy()()

from enum import Enum
Names = Enum("names",("靓仔","校长","鸽吻"))

print(Names(2))
for name,member in Names.__members__.items():
    print(name,member,member.value)

from enum import Enum,unique
@unique
class Address(Enum):
    程序员 = 0
    公务员 = 1
    教师 = 2

print(Address(0),Address(2))

# type() 创建一个新类
def getAge(self):
    return random.randint(20,50)

User_Age =type("User_Age",(object,),dict(getAge = getAge))

print(User_Age().getAge())