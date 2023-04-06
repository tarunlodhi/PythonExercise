mylist = [1,2,3,4,5,6,7,8,9,10]
#Approch 1 using temp variable
'''
temp=mylist[0]
mylist[0]=mylist[-1]
mylist[-1]=temp
'''

#Approch 2:
'''
mylist[0],mylist[-1]=mylist[-1],mylist[0]
'''

#Approch 3 using tuple:
'''
tuple=(mylist[-1],mylist[0])
mylist[0],mylist[-1]=tuple
'''
#Approch 4 * oprand
'''
start,*mid,end=mylist
mylist=[start,*mid,end]
'''

#Approch 5 using buildin function pop()
first = mylist.pop(0)
last = mylist.pop(-1)
mylist.insert(0,last)
mylist.append(first)
print(mylist)

