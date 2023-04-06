number = int(input("Enter The Number :"))
nterms = int(input("Enter The Power :"))

result =list( map (lambda x : number ** x ,range(nterms+1)))
print(result)
for i in range (nterms+1):
    print("the value of {} raised to power {} is : {}".format(number,i,result[i]))