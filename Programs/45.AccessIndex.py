l=[24,74,12,54,68,32,1]
# enumerate
# for index,value in enumerate(l,start=1):
#     print(index,"-",value)

# without enumerate
for i in range(len(l)):
    print(i+1,"-",l[i])