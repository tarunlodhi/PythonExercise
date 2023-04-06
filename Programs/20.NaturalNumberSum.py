num = int(input("Enter the number : "))
sum=0
if num<0:
    print("Please insert +ve interger")
else:
    for i in range(1,num+1):
        sum += i
    print(sum) 