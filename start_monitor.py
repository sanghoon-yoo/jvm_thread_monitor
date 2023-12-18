#!/usr/bin/env python3
# -*-Encoding:UTF-8 -*- #
# -*-coding:utf-8 -*-


import subprocess
import sys
from jstack import *

try:
    pid = sys.argv[1]
    Dump(pid)
    subprocess.Popen(['python3', 'server_monitor.py', pid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('server_monitoring start...')
except JvmException as e:
    print(e)
    pass
except Exception as e:
    if (str(e) == 'list index out of range'):
        print('pid를 입력해주세요')
    else:
        print(e)
    pass
