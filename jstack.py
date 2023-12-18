#!/usr/bin/env python3
# -*-Encoding:UTF-8 -*- #
# -*-coding:utf-8 -*-

from os import *
import time
import sys
from datetime import date
import io
from env import *
from csexception import *

class Dump:
    def __init__(self, pid):
        try:
            self.command = SYSTEM.JAVA.value + str(pid)
            self.stackTrace = self.__read()
        except Exception as e:
            raise

    def __read(self):
        stdout_pipe = popen(self.command)
        response = stdout_pipe.read()
        if (response.find(STATE.THREAD.value)==-1):
            raise JvmException(response)
        return response.split(SYSTEM.NEWLINE.value*2)
    
    def __saveLog(self, data):
        f = io.open(SYSTEM.LOG.getPath(), 'a')
        f.write(SYSTEM.TIMELINE.value + data + SYSTEM.NEWLINE.value*2)
        f.close()

    def getStateCount(self, status, execute=__saveLog):
        self.cnt = 0
        for thread in self.stackTrace:
            if thread.find(str(status))!=-1:
                self.cnt = self.cnt + 1
                execute(self, thread)
        return self.cnt

    def getCpuStatus(self):
        stdout_pipe = popen(SYSTEM.CPU.value)
        return stdout_pipe.read()


if __name__ == "__main__":
    print('noop')

#Dump(811064).getStateCount(STATE.WAITING.value)
#Dump(811064).getCpuStatus()
#Dump(811064).getStateCount(STATE.WAITING.value, lambda x,y: None)

