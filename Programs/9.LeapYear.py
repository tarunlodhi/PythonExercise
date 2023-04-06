number = int(input("Enter A Year :"))

if ((number % 400 == 0) and (number % 100 == 0)) or ((number % 4 == 0) and (number % 100 !=0)):
    print(number," is a leap year")
else:
    print(number," is not a leap year")
