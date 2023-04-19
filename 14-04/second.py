# John:123,Jack:23,Jill:101,Steve:125,Jim:4

input_str = input()
ele_list=[]
final_str =""
ele_list = input_str.split(",")

for ele in ele_list:
    sub_list = ele.split(":")
    name = sub_list[0]
    number = sub_list[1]
    name_length=len(name)

    max =0

    for digit in number:
        if (int(digit)<=name_length):
            if(max<int(digit)):
                max=int(digit)
    if(max==0):
        final_str+='X'
    else:
        final_str+=name[max-1]

print(final_str)