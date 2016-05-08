#-*-coding: UTF-8 -*-

'''
Created on 2016年5月8日

@author: liu
'''


from docutils.utils.math.math2html import Position
from __builtin__ import str
from _ast import Str
import os

os.rename("ok.txt", "foo.txt")
print os.name

fo = open("foo.txt","r+")
'''
print "文件名： ",fo.name
print "是否已关闭： ",fo.close()
print "访问模式： ",fo.mode
print "末尾是否强制加空格： ",fo.softspace
'''
#fo.write("hello world");
str = fo.read(10).encode("utf-8");
print "读取的字符串是： ",str

position = fo.tell()
print "当前的位置是： ",position

position = fo.seek(0,0);
str_01 = fo.read(10);
print "读取的字符串： ",str_01

fo.close()
print "file has been closed"

os.rename("foo.txt", "ok.txt")
print os.name

print os.getcwd()
#os.mkdir("tmp")
os.chdir("tmp")
print os.getcwd()
os.chdir("C:\\00_mywork\\001_work\\10_develop_tools\\workspace\\pyhelloworld\\src")
print os.getcwd()
os.rmdir("tmp")

print "hello test"
print "init test"


