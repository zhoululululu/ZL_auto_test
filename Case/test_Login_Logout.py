# -*- coding: UTF-8 -*-
'''
Created on 2019年03月22日
@author: ZL
'''

from selenium import webdriver
import unittest
from Common.Logout import Logout


class LoginPage(unittest.TestCase):
    def setUp(self):
        chromedriver = "E:/chromedriver/chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.url = 'http://www.raincard.cn/management/login.html'

    def test_Login(self):
        '''验证是否登录成功'''
        Logout.step_login(self, self.driver, self.url)

    def test_Logout(self):
        '''验证账号能否退出'''
        Logout.step_logout(self, self.driver, self.url)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suit = unittest.TestSuite
    runner = unittest.TextTestRunner
    runner.run(suit)
