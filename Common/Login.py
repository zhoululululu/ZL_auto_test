# -*- coding: UTF-8 -*-
'''
Created on 2019年03月19日
@author: ZL
'''

from Data import Config


def step_login(driver, url, username, password):
    config = Config.Config()
    c = config.get_conf()
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_xpath(c['user']).send_keys(username)
    driver.find_element_by_xpath(c['password']).send_keys(password)
    driver.find_element_by_xpath(c['sign']).click()
