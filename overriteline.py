# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 17:31:54 2018

@author: Dhaval
"""
import time, sys
for i in range(6):
    sys.stdout.write("\r" + str(i))
    sys.stdout.flush()
    time.sleep(1)