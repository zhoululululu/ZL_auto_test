# -*- coding: UTF-8 -*-
'''
Created on 2019年03月19日
@author: ZL
'''

import configparser
import os


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Xpath.txt')
        self.config.read(self.conf_path, encoding='UTF-8')

        self.conf = {}

    def get_conf(self):
        #Login
        self.conf['user'] = self.config.get("Login", "user")
        self.conf['password'] = self.config.get("Login", "password")
        self.conf['sign'] = self.config.get("Login", "sign")
        self.conf['title'] = self.config.get("Login", "title")

        #Logout
        self.conf['account'] = self.config.get("Logout", "account")
        self.conf['logout'] = self.config.get("Logout", "logout")

        #Goods
        self.conf['add_goods'] = self.config.get("Goods", "addGoods")
        self.conf['good_name'] = self.config.get("Goods", "goodsName")
        self.conf['good_editor'] = self.config.get("Goods", "goodsEditor")
        self.conf['good_pic'] = self.config.get("Goods", "goodsPic")
        self.conf['good_sku_btn'] = self.config.get("Goods", "goodsSkuBtn")
        self.conf['sku_name'] = self.config.get("Goods", "skuName")
        self.conf['sku_value'] = self.config.get("Goods", "skuValue")
        self.conf['sku_pic'] = self.config.get("Goods", "skuPic")
        self.conf['sku_price'] = self.config.get("Goods", "skuPrice")
        self.conf['sku_stock'] = self.config.get("Goods", "skuStock")
        self.conf['sku_num'] = self.config.get("Goods", "skuNum")
        self.conf['sku_group'] = self.config.get("Goods", "goodsGroup")
        self.conf['good_category'] = self.config.get("Goods", "goodCategory")


        #Email
        self.conf['login_email'] = self.config.get("email", "login_email")
        self.conf['login_password'] = self.config.get("email", "login_password")
        self.conf['port'] = self.config.get("email", "port")
        self.conf['smtp'] = self.config.get("email", "smtp")
        self.conf['Recipient'] = self.config.get("email", "Recipient")
        self.conf['subject'] = self.config.get("email", "subject")
        self.conf['mailbody'] = self.config.get("email", "mailbody")

        return self.conf
