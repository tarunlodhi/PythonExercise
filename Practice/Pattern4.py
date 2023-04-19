"""
Pattern
P
Py
Pyt
Pyth
Pytho
Python
"""
str = input("Enter The String : ")
k = len(str)
for row in range(k):
    for col in range (0,row+1):
        print(str[col],end="")
    print()

n=6
a,b=0,1
print(a,b,"",end="")
sum = 0
for i in range(2,n):
    sum = a+b
    print(sum,end=" ")
    a=b
    b=sum

