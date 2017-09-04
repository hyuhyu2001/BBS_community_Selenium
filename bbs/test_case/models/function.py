#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:定义截图函数
"""

from selenium import webdriver
import os

def insert_img(driver,file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    print(base_dir)
    base_dir = str(base_dir)
    print(base_dir)
    base_dir = base_dir.replace('\\','/')
    print(base_dir)
    base = base_dir.split('/test_case')[0]
    print(base)
    file_path = base + r"/report/image/" + file_name
    print(file_path)
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    dr = webdriver.Firefox()#打开chrome浏览器的时候无法截图
    dr.get("http://www.baidu.com")
    insert_img(dr,'baidu.jpg')
    dr.quit()