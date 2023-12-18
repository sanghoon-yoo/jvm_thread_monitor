#!/usr/bin/env python3
# -*-Encoding:UTF-8 -*- #
# -*-coding:utf-8 -*-


from jstack import *
import time
from env import *
from csexception import *

pid = sys.argv[1]
try:
    while True:
        try:
            dumping = Dump(pid)
        except JvmException as e:
            print(e)
            break
        if (dumping.getStateCount(STATE.BLOCKED.value)):
            dumping.getCpuStatus()
            #print(dumping.getCpuStatus())
            #print(dumping.getStateCount(STATE.NEW.value, lambda x,y: None))
            #print(dumping.getStateCount(STATE.RUNNABLE.value, lambda x,y: None))
            #print(dumping.getStateCount(STATE.TIMED_WAITING.value, lambda x,y: None))
            #print(dumping.getStateCount(STATE.WAITING.value, lambda x,y: None))
            #print(dumping.getStateCount(STATE.BLOCKED.value, lambda x,y: None))
        time.sleep(int(SYSTEM.INTERVAL.getInterval()))
except KeyboardInterrupt:
    print('cancel')



    
