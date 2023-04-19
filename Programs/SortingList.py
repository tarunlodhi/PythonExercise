list = [1,9,7,5,2]

for i in range(len(list)):
    # print(list[i])
    min_value = list[i]
    for j in range(len(list)):
        if min_value < list[j]:
            list[i],list[j]=list[j],list[i]

print(list)
