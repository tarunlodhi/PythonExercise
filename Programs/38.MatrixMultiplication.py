X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,4],
    [4,5,9,7]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

'''
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] *Y[k][j]

for i in result:
    print (i)'''


result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)