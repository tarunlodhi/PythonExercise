"""
pattern
1
23
456
78910
"""
n = int(input("enter the number"))
num = 1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num =num +1
    print("")