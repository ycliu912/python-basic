#-*-coding:utf-8 -*-
'''
Created on 2016年5月5日

@author: liu
'''

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938477567
phonebook["Jill"] = 938477568

'''
phonebook = {
    "John" : 938477566,
    "Jack" : 938477567,
    "Jill" : 938477568
}
'''

#del phonebook["John"]
#phonebook.pop("Jill")
phonebook["July"] = 938477569

for name,number in phonebook.iteritems():
    print "Phone number of %s is %d" % (name,number)

