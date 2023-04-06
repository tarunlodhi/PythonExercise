mylist =[5,1,6,8,4,2,5,3,9,4,7,1,36,5,5]
count = 0
n=5
'''     #1
for i in mylist:
    if i==n:
        count= count+1

print("{} has occured {} of times".format(n,count))
'''
'''         #2
print("{} has occured {} of times".format(n,mylist.count(n)))
'''

from collections import Counter

dic = Counter(mylist)
print("{} has occured {} of times".format(n,dic[n]))