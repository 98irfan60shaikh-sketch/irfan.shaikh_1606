a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    print(f"The largest number is: {a}")
else:
    if b > a and b > c:
        print(f"The largest number is: {b}")
    else:
        print(f"The largest number is: {c}")