a = input("Enter a sentance : ")
vowel = "aeiou"

a=a.casefold()
print(a)

count ={}.fromkeys(vowel,0)
for char in a:
    if char in count:
        count[char] +=1

print(count)

