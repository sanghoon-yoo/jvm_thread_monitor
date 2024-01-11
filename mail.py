#!/usr/bin/env python3
# -*-Encoding:UTF-8 -*- #
# -*-coding:utf-8 -*-



import smtplib
from email.mime.text import MIMEText
from csexception import *
from env import *
import platform

class Mail:
    def __init__(self):
        try:
            self.smtp = smtplib.SMTP('', 25)
            self.smtp.ehlo()
            self.smtp.login(MAIL.PROP.getSender(), MAIL.PROP.getPassword())
        except Exception as e:
            raise MailException('메일서버 연결실패 : ' + str(e))

    def send(self, msg):
        msg = MIMEText(msg)
        msg['From'] = ''
        msg['Subject'] = platform.uname().node + '서버 부하 상태 알림'
        msg['To'] = ''

        for receiver in MAIL.PROP.getReceiver().split(','):
            self.smtp.sendmail(MAIL.PROP.getSender(), receiver, msg.as_string())
        self.smtp.quit()

