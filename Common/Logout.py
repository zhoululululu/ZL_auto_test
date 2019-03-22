# -*- coding: UTF-8 -*-
'''
Created on 2018年05月22日
@author: ZL
'''

import time
from Common.Login import *


class Logout:
    config = Config.Config()
    c = config.get_conf()

    # 能否正常登录
    def step_login(self, driver, url):
        step_login(driver, url, '18817933821', '123456')
        driver.implicitly_wait(15)
        title = driver.find_element_by_xpath(Logout.c['title']).text
        tm = time.strftime('%H:%M:%S', time.localtime(time.time()))
        if tm > '12:00:00':
            self.assertTrue(title == '下午好，18817933821')
        else:
            self.assertTrue(title == '早上好，18817933821')

    # 首页-能否正常退出
    def step_logout(self, driver, url):
        step_login(driver, url, '18817933821', '123456')
        time.sleep(12)
        driver.find_element_by_xpath(Logout.c['account']).click()
        driver.find_element_by_xpath(Logout.c['logout']).click()
        time.sleep(3)
        url = self.driver.current_url
        self.assertTrue(url == 'http://www.raincard.cn/management/login.html')
