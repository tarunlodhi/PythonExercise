number = int(input("Enter The Number : "))

for i in range(2,number+1):
    if number%i == 0:
        print("The factor of {} number is : {}".format(number,i))