def fact(n):
    if n ==1:
        return 1
    else:
        return (n * fact(n-1))
    
n = int(input("Enter a number : "))
if n<=0:
    print("Enter a positive number")
else:
    print("Factorial of {} number is ".format(n),fact(n))