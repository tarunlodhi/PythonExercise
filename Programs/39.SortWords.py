words = input("Enter sentance here :")
list = words.split()

for i in range(len(list)):
    list[i] = list[i].lower()


list.sort()

print(" ".join(list))