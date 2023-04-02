'''0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233'''
start = 0
second = 1

num = int(input("Enter the Number to obtain fibonacci sequence :"))

if num <= 0:
    print("There is no sequence of number 0 and less")
elif num == 1:
    print(start)
elif num == 2:
    print(start,second)
else:
    fibo=[start,second]
    for i in range(2,num):
        sequence = start + second
        start = second
        second= sequence
        fibo.append(sequence)
    print(fibo)