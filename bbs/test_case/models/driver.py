#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:配置测试用例在不同的主机及浏览器下运行
"""

from selenium import webdriver
from selenium.webdriver import Remote

#启动浏览器驱动
def browser():
    # driver = webdriver.Chrome()
    host = '127.0.0.1:4444'
    dc = {'browserName':'charome'}
    driver = Remote(command_executor='http://'+host+'/wd/hub',desired_capabilities=dc)
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()