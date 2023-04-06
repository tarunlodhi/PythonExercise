num = int(input("Enter The number :"))
n1 = 0
n2 = 1

if (num<=0):
    print("There is no Fibonacci Series of negetive and zero number")
elif(num==1):
    print(n1)
elif(num==2):
    print(n1)
    print(n2)
else:
    print(n1)
    print(n2)
    for i in range(2,num):
        sum = n1 + n2
        print(sum)
        n1=n2
        n2=sum