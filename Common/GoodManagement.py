# -*- coding: UTF-8 -*-
'''
Created on 2019年03月22日
@author: ZL
'''

import time
from Common import Login
from Common.public_model import *
from selenium.webdriver.support.wait import WebDriverWait
from Data import Config
from Common import PublicModel


class GoodsManagement:
    config = Config.Config()
    c = config.get_conf()

    # 商品管理-添加商品
    def step_add_good(self, driver, url, model_name):
        Login.step_login(driver, url, '18817933821', '123456')
        time.sleep(3)
        PublicModel.select_model(driver, model_name)
        time.sleep(5)
        driver.find_elements_by_xpath(GoodsManagement.c['add_goods']).click()
        time.sleep(3)
        driver.find_elements_by_xpath(GoodsManagement.c['add_goods']).send_keys("测试商品")
        driver.find_elements_by_xpath(GoodsManagement.c['goodsEditor']).send_keys("测试商品信息")
        driver.find_elements_by_xpath(GoodsManagement.c['goodsPic']).send_keys("E:\Pycharm\workspace\ZL_AutoTest\Data\pic.jpg")
        driver.find_elements_by_xpath(GoodsManagement.c['goodsSkuBtn']).click()
        driver.find_elements_by_xpath(GoodsManagement.c['skuName']).send_keys("测试SKU")
        driver.find_elements_by_xpath(GoodsManagement.c['skuValue']).send_keys("测试SKU Value"+"\n")
        driver.find_elements_by_xpath(GoodsManagement.c['skuPic']).send_keys("E:\Pycharm\workspace\ZL_AutoTest\Data\pic.jpg")
        driver.find_elements_by_xpath(GoodsManagement.c['skuPrice']).send_keys("0.01")
        driver.find_elements_by_xpath(GoodsManagement.c['skuStock']).send_keys("10")
        driver.find_elements_by_xpath(GoodsManagement.c['skuNum']).send_keys("SKU123456")
        driver.find_elements_by_xpath(GoodsManagement.c['goodsGroup']).click()
        driver.find_elements_by_xpath(GoodsManagement.c['good_category']).click()