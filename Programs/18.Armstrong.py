"""153 = (1*1*1)+(5*5*5)+(3*3*3)  
where:  
(1*1*1)=1  
(5*5*5)=125  
(3*3*3)=27  
So:  
1+125+27=153"""

nuber = str(input("Enter the number to check Armstrong digit number :"))
number = len(nuber)
k= int(nuber)
tot =0
for i in nuber:
    j = int(i)
    sum = j**number
    tot += sum
if(tot==k):
    print("{} is a Armstrong Number".format(nuber))
else:
    print("{} is not an Armstrong Number".format(nuber))

# num = int(input("Enter the Number :"))
# sum=0
# temp=num
# while temp>0:
#     digit = temp%10
#     cube = digit**3
#     sum = sum + cube
#     temp //= 10
# if(sum==num):
#     print(" Armstrong Number")
# else:
#     print("Not an Armstrong Number")