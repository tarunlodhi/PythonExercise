list = [1,5,7,8,9,5,44,7,23,6,4]
# print(list[::2])
# print(list[1::2])

sum= 10
print(len(list))
for i in range(len(list)-1):
    if sum ==list[i]+list[i+1]:
        print ("The sum found at index : ",i,i+1)