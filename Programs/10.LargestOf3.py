x = float(input("Enter the number 1 : "))
y = float(input("Enter the number 2 : "))
z = float(input("Enter the number 3 : "))

if x>y and x>z:
    print(x,"is largest number")
elif y>x and y>z:
    print(y,"is largest number")
else:
    print(z,"is largest number")