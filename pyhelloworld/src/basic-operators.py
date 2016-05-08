#-*-coding:utf-8 -*-
'''
Created on 2016年5月5日

@author: liu
'''
from argparse import REMAINDER
import lists

number = 1 + 2 * 3 / 4.0
remainder = 11 % 3
squared = 7 ** 2
cubed = 2 ** 3
helloworld = "hello" + " " + "world"
lotsofhellos = "hello" * 10

print number
print remainder
print squared
print cubed
print helloworld
print lotsofhellos

print lists.__name__
print lists.__file__
print lists.mylist
print lists.x
print lists.__dict__