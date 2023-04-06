num = int(input("Enter the number :"))

def factorial(n) :
    # if (n == 0 or n==1):
    #     return 1
    # else:
    #     return n*factorial(n-1)
    
    #ternary oprater 
    return 1 if(n == 0 or n==1) else n*factorial(n-1)

print("factorial of num {} is :".format(num) ,factorial(num))
