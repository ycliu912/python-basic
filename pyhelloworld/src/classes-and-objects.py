#-*-coding:utf-8 -*-
'''
Created on 2016年5月5日

@author: liu
'''

class MyClass:
    variable = "blah"
    
    def function(self):
        print "This is a message inside the class."

myobjectx = MyClass()

print myobjectx.function()
print '11111111111111'
print myobjectx.variable
print '22222222222222222'

myobjecty = MyClass()
myobjecty.variable = "yackity"
print myobjectx.variable
print myobjecty.variable
print myobjecty.function()


#define the Vehicle class
class Vehicle:
    name = ""
    kind = ""
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name,self.color,self.kind,self.value)
        return desc_str
# your code goes her

car1 = Vehicle()
car1.name = "a-car"
car1.kind = "myself"
car1.color = "red"

#print car1.description()

car2 = Vehicle()
car2.name = "b-car"
car2.kind = "company"
car2.color = "blue"
car2.value = 1000.00

print car1.description()
print car2.description()

#myVehicle = Vehicle()



# test code
#print car1.description()
#print car2.description()