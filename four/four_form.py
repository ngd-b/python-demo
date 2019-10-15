#!/usr/bin/python
# -*- coding:utf-8 -*-

# 自定义表单校验错误类
class ConflictValueError(ValueError):
    pass

class ExistError(ValueError):
    pass

class PureNumberError(ValueError):
    pass

class LenError(ValueError):
    pass
# 表单用户名校验 、 不能是纯数字、不能有特殊符号、必须6位以上
import re
class ValidForm():
    '''
    valid name
    >>> ValidForm().exist_name()
    Traceback (most recent call last):
    ...
    ExistError: 必须填写用户名!
    >>> ValidForm(**{"name":"ad_min"}).conflict_name()
    Traceback (most recent call last):
    ...
    ConflictValueError: 你不能使用这个名字
    >>> ValidForm(**{"name":"admin_123"}).isAvailable()
    True
    '''
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

# ValidForm(**{"name":"admin_123"}).isAvailable()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
