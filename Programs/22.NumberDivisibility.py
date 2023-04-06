divisor = int(input("Enter the divisor to check : "))
lower = int(input("Enter the lower digit : "))
upper = int(input("Enter the upper digit : "))
for i in range(lower,upper):
    if i % divisor == 0:
        print(i)