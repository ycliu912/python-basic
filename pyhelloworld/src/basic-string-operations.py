#-*-coding:utf-8 -*-
'''
Created on 2016年5月5日

@author: liu
'''

astring = "Hello world!"
astring2 = 'Hello world!'

print "single quotes are ' '"
print len(astring)

print astring.index("o")
print astring.count("1")
print astring[3:7]
print astring[3:7:2]

print astring[::-1]
print astring.upper()
print astring.lower()

print astring.startswith("Hello")
print astring.endswith("asdfasdfasdf")

afewwords = astring.split(" ")
print afewwords