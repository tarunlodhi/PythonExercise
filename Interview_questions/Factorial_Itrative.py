num = int(input("Enter the number :"))
factorial = 1
if num < 0:
    print("Factorial of negative number doesnt exist")
elif num == 0 or 1:
    print("Factorial of {} number is 1".format(num))
else:
    for i in range(1,num):
        factorial= factorial*i
    print("factorial of number {} is :".format(num), factorial)