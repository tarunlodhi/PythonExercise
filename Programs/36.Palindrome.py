string = input("enter the string to check Palindrome : ")
rev = string[::-1]
if string==rev:
    print("{} is a Palindrome".format(rev))
else:
    print("{} is not Palindrome".format(string))