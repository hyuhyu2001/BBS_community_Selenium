#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:用户登陆页面
"""

from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class Login(Page):
    '''用户登陆页面'''

    url = '/'

    #Action
    bbs_login_user_loc = (By.XPATH,"//div[id='mzCust]/div/img")
    bbs_login_button_loc = (By.ID,'mzLogin')

    def bbs_login(self):
        self.find_element(*self.bbs_login_user_loc).click()
        sleep(1)
        self.find_element(*self.bbs_login_button_loc).click()

    login_username_loc = (By.ID,'account')
    login_password_loc = (By.ID, 'password')
    login_button_loc = (By.ID, 'lpgin')

    #登陆用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登陆密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登陆按钮
    def login_button(self,):
        self.find_element(*self.login_button_loc).click()

    #定义统一登陆入口
    def user_login(self,username='username',password='1111'):
        '''获取用户名和密码登陆'''
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    user_error_hint_loc = (By.XPATH,"//span[@for='account']")
    pawd_error_hint_loc = (By.XPATH,"//span[@for='password']")
    user_login_success_loc = (By.ID,"mzCustName")

    #用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    #密码错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text

    #登陆成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text