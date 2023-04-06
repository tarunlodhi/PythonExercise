list = ["shivam","eats","banana","shivam","eats","banana","shivam","eats","banana"]
word ="shivam"
n=2;
count=0

for i in range(0,len(list)-1):
    if(list[i]==word):
        count = count+1
        if count == n:
            print (i)
            del list[i]
print(list)