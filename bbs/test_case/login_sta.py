#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:编写测试用例，与loginPage的登陆对象保持名字前缀一致，方便后期维护修改
"""

from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login

class loginTest(myunit.MyTest):
    '''社区登录测试'''

    #测试用户登陆
    def user_login_verify(self,username='',password=''):
        login(self.driver).user_login(username,password)

    def test_login1(self):
        '''用户名、密码为空登陆'''
        self.user_login_verify()
        po= login(self.driver)
        self.assertEqual(po.user_error_hint(),"账户不能为空")
        self.assertEqual(po.pawd_error_hint(), "密码不能为空")
        function.insert_img(self.driver,"user_pawd_empty.jpg")

    def test_login2(self):
        '''用户名、密码正确登陆'''
        self.user_login_verify(username='zhangsan',password='123456')
        sleep(2)
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), "张三")
        function.insert_img(self.driver, "user_pawd_true.jpg")

if __name__ == '__main__':
    unittest.main()