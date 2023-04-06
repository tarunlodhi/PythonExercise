def fiboo(n):
    if n<=1:
        return n
    else:
        return fiboo(n-1) + fiboo(n-2)

n = int(input("Enrter the number"))

if n<0:
    print("enter positive number")
else :
    print ("fibonacci Sequence")
    for i in range(n):
        print(fiboo(i))