# -*- coding: UTF-8 -*-
'''
Created on 2019年03月22日
@author: ZL
'''

from selenium.webdriver.support.wait import WebDriverWait

class PublicModel():
    def select_model(driver, model_name):
        elements = driver.find_elements_by_tag_name('li')
        for i in elements:
            if i.text == model_name:
                i.click()
                break

                # 等待时间
    def Wait_element(driver, element, value):
        WebDriverWait(driver, 10).until(lambda x: x.element).send_keys(value)