#!/usr/bin/env python3
# -*-Encoding:UTF-8 -*- #
# -*-coding:utf-8 -*-


from enum import Enum
from os import *
from datetime import datetime
from datetime import date
import configparser

class STATE(Enum):
    THREAD = 'java.lang.Thread.State'
    NEW = 'State: NEW'
    RUNNABLE = 'State: RUNNABLE'
    BLOCKED = 'State: BLOCKED'
    WAITING = 'State: WAITING'
    TIMED_WAITING = 'State: TIMED_WAITING'

    def __repr__(self):
        return str(self.value)

class SYSTEM(Enum):
    def __init__(self, code):
        self.config = configparser.ConfigParser()
        self.config.read('monitoring.properties')

    def __repr__(self):
        return str(self.value)

    def getPath(self):
        return self.config.get('LOG','PATH') + '/jvm_threads_dump.log.' + date.today().strftime('%Y%m%d')

    def getInterval(self):
        return self.config.get('LOG','INTERVAL')

    NEWLINE = '\n'
    JAVA = getenv('JAVA_HOME') + '/bin/jstack '
    TIMELINE = '[' + str(datetime.now()) + ']'
    CPU = "top -bn1 | grep 'Cpu(s)' | awk '{printf(\"CPU 사용률 : %.1f%%\\n\", 100 - $8)}'"
    LOG = ''
    INTERVAL = ''
    
