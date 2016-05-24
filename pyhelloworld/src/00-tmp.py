#!/usr/bin/env python
#coding:utf-8
from itertools import count
import time

count = 1
while True:
    print "just a test '%s'"%count
    time.sleep(3)
    count = count + 1
