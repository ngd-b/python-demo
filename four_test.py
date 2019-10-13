#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest

from four_form import ValidForm,ExistError,ConflictValueError,LenError

class TestValidForm(unittest.TestCase):
    # 在每个测试方法开始前调用 before
    def setUp(self):
        pass
        # print("start->", end="")
    def test_existError(self):
        with self.assertRaises(ExistError):
            ValidForm().exist_name()

    def test_conflicError(self):
        with self.assertRaises(ConflictValueError):
            ValidForm(**{"name":"admin"}).conflict_name()
    @unittest.skip("将不会被调用")
    def test_lenError(self):
        with self.assertRaises(LenError):
            ValidForm(**{"name":"abc"}).len_name()
    # 方法调用后执行
    def tearDown(self):
        pass
        #print("end \n",end="")

if __name__ == '__main__':
    unittest.main()