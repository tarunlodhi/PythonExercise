def fun(inputs):
    stack=[]
    c=0
    for ele in inputs:
        if (ele=="{" or ele=="[" or ele =="("):
            stack.append(ele)
            c+=1
            continue
        if (len(stack)==0):
            return c+1
        temp = stack.pop()
        if(ele=="]" and temp =="["):
            c+=1
        if(ele==")" and temp =="("):
            c+=1
        if(ele=="}" and temp =="{"):
            c+=1
    if (len(stack))==0:
        return 0
    else:
        return c+1

inputs = input()
res=fun(inputs)
print(res)