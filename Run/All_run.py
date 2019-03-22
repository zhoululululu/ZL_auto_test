# -*- coding: UTF-8 -*-
'''
Created on 2019年03月22日
@author: ZL
'''
import os
import sys
import time
import unittest
from Common import SendEmail

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]

sys.path.append(rootPath)
from HTMLTestRunner import HTMLTestRunner


def Add_case():
    test_dir = rootPath + '\Case'
    suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    print(discover)
    for test_suit in discover:
        for case in test_suit:
            suit.addTest(case)
    return suit


alllcase = Add_case()
now = time.strftime('%y_%m_%d-%H_%M_%S')
filename = rootPath + '\Report' + '\\' + now + 'result.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner(stream=fp, title='标准产品平台UI测试报告', description='测试执行情况')
runner.run(alllcase)
SendEmail.send_email(filename)
