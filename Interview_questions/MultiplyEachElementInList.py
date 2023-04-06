mylist=[1,2,3,4]

''' Method #1
total = 1
for i in mylist:
    total*=i
print("Multipling using for loop :", total)
'''
import numpy
result=numpy.prod(mylist)
print (result)