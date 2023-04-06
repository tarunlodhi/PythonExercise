'''Approach 1 using slicing techinque
Approach 2 using extend() method 
Approach 3 Using the list() method
Approach 4 Using the copy() method 
Approach 5 using list comprehension'''
mylist =[9, 8, 7, 6, 5, 4, 3, 2, 1]
'''     #1
copy_list = mylist[:]
print (copy_list) '''

'''    #2
copy_list = []
copy_list.extend(mylist)
print(copy_list) '''

'''        #3
copy_list = list(mylist)
print (copy_list)'''

'''         #4
copy_list=mylist.copy()
print (copy_list) '''

            #5
copy_list = [i for i in mylist]
print(copy_list)