array=[21,54,32,1,2,3,4,5,6,7,8,9,10]

max = array[0]
total_elements = len(array)
#finding maximum value
for i in range(1,total_elements):
    if array[i] > max:
        max = array[i]

print("Maximum number is :",max)

#finding minimum value
min=array[0]
for i in range(1,total_elements):
    if array[i] < min:
        min = array[i]

print("Minimum number is :",min)