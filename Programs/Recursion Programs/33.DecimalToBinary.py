def ConvertBinary(n):
    if n > 1:
        ConvertBinary(n//2)
    print(n%2,end="")

print("the binary of the given number is :")
ConvertBinary(20)