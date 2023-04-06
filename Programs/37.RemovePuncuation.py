pun = ('''~`!@#$%^&*()_+=}{[]\|"';:<.>,/?''')

string = input("enter anything :")
emt_str = ""

for i in string:
    if i not in pun:
        emt_str +=i

print(emt_str)