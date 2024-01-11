#!/usr/bin/env python3
# -*-Encoding:UTF-8 -*- #
# -*-coding:utf-8 -*-


from jstack import *
import time
from env import *
from csexception import *
from mail import *

pid = sys.argv[1]

try:
    while True:
        try:
            dumping = Dump(pid)
        except JvmException as e:
            print(e)
            break
        if (dumping.getStateCount(STATE.BLOCKED.value, lambda x,y: None)>=5):
            msg = dumping.getCpuStatus() + SYSTEM.NEWLINE.value + dumping.getDiskStatus() + SYSTEM.NEWLINE.value + dumping.getRamStatus()
            msg = msg + SYSTEM.NEWLINE.value + STATE.BLOCKED.value + ' count : ' + str(dumping.getStateCount(STATE.BLOCKED.value))
            msg = msg + SYSTEM.NEWLINE.value + STATE.NEW.value + ' count : ' + str(dumping.getStateCount(STATE.NEW.value, lambda x,y: None))
            msg = msg + SYSTEM.NEWLINE.value + STATE.WAITING.value + ' count : ' + str(dumping.getStateCount(STATE.WAITING.value, lambda x,y: None))
            msg = msg + SYSTEM.NEWLINE.value + STATE.TIMED_WAITING.value + ' count : ' + str(dumping.getStateCount(STATE.TIMED_WAITING.value, lambda x,y: None))
            msg = msg + SYSTEM.NEWLINE.value + STATE.RUNNABLE.value+ ' count : ' + str(dumping.getStateCount(STATE.RUNNABLE.value, lambda x,y: None))
            Mail().send(msg)
        time.sleep(int(SYSTEM.INTERVAL.getInterval()))
except KeyboardInterrupt:
    print('cancel')
except Exception as e:
    print(e)

