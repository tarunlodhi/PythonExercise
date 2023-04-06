print("~~~~~~calculator~~~~~~")
first = float(input("Enter the first number : "))
second = float(input("Enter the second number : "))

print("press 1 for addition \n press 2 for subtraction \n press 3 for multiplication \n press 4 for division")
choice = int(input("enter your choice : "))
if choice==1:
    print(first+second)
elif choice == 2:
    print(first-second)
elif choice==3:
    print(first*second)
elif choice==4:
    if first==0:
        print(first)
    elif second==0:
        print("infinit")
    else:
        print(first/second)
else:
    print("Please select from 1-4 only")
