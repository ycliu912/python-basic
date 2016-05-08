#-*-coding:utf-8 -*-
'''
Created on 2016年5月5日

@author: liu
'''

primes = [1,3,5,7]
for prime in primes:
    print prime
for x in xrange(5):
    print x
print '------------------------------------------------------------'

for x in xrange(3,6):
    print x
print '------------------------------------------------------------'

for x in xrange(3,8,2):
    print x

print '------------------------------------------------------------'  
count = 0
while count < 5:
    print count
    count += 1
    
count = 0
while True:
    print count
    count += 1
    if count >= 5:
        break
    
print '------------------------------------------------------------'  
 

for x in xrange(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print x
 
    
for x in xrange(10):
    if x % 2 == 0:
        continue
    print x


count=0
while(count<5):
    print count
    count = count + 1
else:
    print "count value reached %d" %(count)

   
for i in xrange(1,10):
    if(i%5==0):
        break
    print i
else:
    print "this is not printed because for loop is terminated because of break but not due to fail in condition"
  
