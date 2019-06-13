#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import smtplib


host = 'smtp.163.com'
sender = 'gaoyx213@163.com'

message = '''From: From Person <gaoyx213@163.com>
To: To Person <gaoyx213@163.com>
Subject: SMTP e-mail test

THIS IS A TEST MESSAGE.
'''

receivers = ['gaoyx213@163.com']

try:
    server = smtplib.SMTP("smtp.163.com")
    server.login('gaoyx213@163.com', 'xxxxxxxx')
    server.sendmail(sender, receivers, message)
    server.quit()
    print("Successfully sent email.")
except Exception as e:
    print("Error: unable to send email")
    raise e


