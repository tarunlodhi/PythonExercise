given_number = input()
length_given_number =len(given_number)
otp=""
for i in range (1,length_given_number,2):
    odd = int(given_number[i])
    odd = odd**2
    otp+=str(odd)

print(otp[0:4])