num =int(input("Enter the natural number :"))
count = 0

if num<=0:
    print("its not a natural number")
else:
    for i in range(1,num+1):
        if (num%i)==0:
            count=count+1
    if(count==2):
        print("Number {} is prime".format(num))
    else:
        print("Number {} is not prime".format(num))