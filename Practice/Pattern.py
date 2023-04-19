"""
Pattern
1
12
123
1234
12345
"""

n = int(input("Enter the Number :"))
for i in range(1,n+1):
    for j in range (1,i+1):
        print(j,end="")
    print()

"""
Pattern 2
1
22
333
4444
55555
"""
for i in range(1,n+1):
    for j in range (1,i+1):
        print(i,end="")
    print()