n=6
"""
pattern
*     
**    
* *
*  *
*   *
******
"""
for row in range(n):
    for col in range(n):
        if col==0 or row==(n-1) or row==col: 
            print("*",end="")
        else:
            print(end=" ")
    print()

"""
pattern
*
**
***
****
*****
******
"""
for row in range(1,n+1):
    for col in range(1,row+1):
        print("*",end="")
    print()