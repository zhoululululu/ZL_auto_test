# -*- coding: UTF-8 -*-
'''
Created on 2019年03月22日
@author: ZL
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
from Data import Config


def send_email(file):
    # 配置文件中
    config = Config.Config()
    c = config.get_conf()
    smtp_email = c["smtp"]
    port = c["port"]
    login_email = c["login_email"]
    login_password = c["login_password"]
    subject = c["subject"]
    Recipient = c["Recipient"]
    mailbody = c["mailbody"]

    smtp = smtplib.SMTP_SSL(smtp_email, port)
    smtp.login(login_email, login_password)

    att = MIMEApplication(open(file, 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename="report.html")

    msgRoot = MIMEMultipart('related')
    msgRoot['To'] = Recipient
    msgRoot['From'] = login_email
    msgRoot['Subject'] = Header(subject, 'gb2312')
    msg = MIMEText(mailbody, 'html', 'utf-8 ')
    msgRoot.attach(msg)
    msgRoot.attach(att)

    try:
        smtp.sendmail(login_email, Recipient, msgRoot.as_string())
        print("发送成功")
    finally:
        smtp.close
