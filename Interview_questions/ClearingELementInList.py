'''
#using clear() method
list = [1,2,3,4,5,6,7,8,9,0]
print("list before clearing",list)
list.clear()
print("list after clearing",list)
'''
'''
#clear using forloop and pop
list = [1,2,3,4,5,6,7,8,9,0]
print("list before clearing",list)
for i in range(len(list)):
    list.pop()
print("list after clearing",list)
'''
'''
#Assigning Empty list
list = [1,2,3,4,5,6,7,8,9,0]
print("list before clearing",list)
list=[]
print("list after clearing",list)
'''
'''
#using *=0
list = [1,2,3,4,5,6,7,8,9,0]
print("list before clearing",list)
list *=0
print("list after clearing",list)
'''

#using del 

list = [1,2,3,4,5,6,7,8,9,0]
print("list before clearing",list)
del list[:]
print("list after clearing",list)