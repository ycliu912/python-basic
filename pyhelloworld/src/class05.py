#-*-coding:utf-8 -*-
'''
Created on 2016年5月10日

@author: liu
'''

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
        
    def __str__(self):
        return "Vector (%d, %d)" % (self.a, self.b)
    
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)
    
V1 = Vector(2,10)
V2 = Vector(5,-2)
print V1 + V2    
    
