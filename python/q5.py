n = int(input("Enter the number: "))
num = 1
i = 1

while i <= n:
    j = 1
    while j <= i:   
        print(num, end=" ")
        num += 1
        j += 1
    print()       
    i += 1