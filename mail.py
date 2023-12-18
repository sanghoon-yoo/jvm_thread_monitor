#!/usr/bin/env python3
# -*-Encoding:UTF-8 -*- #
# -*-coding:utf-8 -*-



import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP_SSL('', 25)
smtp.ehlo()

smtp.login('', '')

msg = MIMEText('테스트')
msg['From'] = ''
msg['Subject'] = '테스트입니다'
msg['To'] = ''

smtp.sendmail('', '', msg.as_string())
smtp.quit()
