#-*-coding:utf-8 -*-
'''
Created on 2016年5月10日

@author: liu
'''

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name,"销毁"

pt1 = Point()
pt2 = pt1
pt3 = pt1

print id(pt1), id(pt2), id(pt3)
del pt1
del pt2
del pt3
