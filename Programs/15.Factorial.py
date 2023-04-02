'''
num = int(input("Enter the number : "))
factorial=1
if num<0:
    print("Factorial less then 0 doesnt exists")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = i*factorial
    print ("The factorial of given number is :",factorial)
'''

#Using Recursion
def fact(a):
    if a == 0:
        return 1
    else:
        return((a)*fact(a-1))

num = int(input("Enter The Number"))
result = fact(num)
print("The factorial of given number is :",result)