#-*-coding:utf-8 -*-
'''
Created on 2016年5月5日

@author: liu
'''

def my_function():
    print "Hello from My Function!"
my_function()

def my_function_with_args(username,greeting):
    print "Hello,%s,From My Function! I wish you %s" %(username,greeting)
my_function_with_args("liu", "well!")

def sum_two_number(a,b):
    return a + b
print sum_two_number(1, 2)