list =[5,9,7,6,4,2,1,4,6]
'''
#Approach 1 using for loop
n = 6
count=0
for i in range(0,len(list)):
    if list[i]==n:
        print("First element found is found at index",i)
        count = 1
        break

if count == 0:
    print("element not found")
'''
n=3
if (n in list):
    print("element found")
else:
    print("element not found")