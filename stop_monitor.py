#!/usr/bin/env python3
# -*-Encoding:UTF-8 -*- #
# -*-coding:utf-8 -*-


import psutil
import time

for proc in psutil.process_iter(['pid','cmdline']):
    if 'server_monitor.py' in proc.info['cmdline']:
        print(str(proc.info['pid']) + ' stoped')
        psutil.Process(proc.info['pid']).terminate()
        break
