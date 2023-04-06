sent = "This handy tool helps you create dummy text for all your layout needs. We are gradually adding new functionality and we welcome your suggestions and feedback."
str = input("Enter the Word to find : ")
'''# Finding without using any function
word = sent.split(" ")
print(word)
count = 0
for i in word:
    if str==i:
        print("word found")
        count = 1
        break
if count == 0:
    print("word not found")
    '''

#Using Find function
if sent.find(str) == -1:
    print("Word Not Found")
else:
    print("Word Found")