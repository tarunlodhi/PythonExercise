#swaping element 1,3 index
my_list = [25,12,49,16,74]
print("My List :" ,my_list)
num1,num2=1,3
my_list[num1],my_list[num2]=my_list[num2],my_list[num1]
print("Swap normally :" ,my_list)
print("New List :" ,my_list)
first = my_list.pop(num1)
second = my_list.pop(num2-1)
my_list.insert(num1,second)
my_list.insert(num2,first)
print("Swap using pop function :" ,my_list)

print("New List :" ,my_list)
tuple = (my_list[num2],my_list[num1])
my_list[num1],my_list[num2] = tuple
print("Swap using tuple :" ,my_list)