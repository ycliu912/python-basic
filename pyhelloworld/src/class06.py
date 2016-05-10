#-*-coding:utf-8 -*-
'''
Created on 2016年5月10日

@author: liu
'''

class JustCounter:
    __secretCount = 0  #私有变量
    publicCount = 0    #共有变量
    
    
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount
        
        
counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
print counter.__secretCount   #报错，实例不能访问私有变量