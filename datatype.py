value = input("Enter something: ")

if value.isdigit():
    print("You entered a number.")
    print("Data type:", type(int(value)))

elif len(value) == 1 and value.isalpha():
    print("You entered a character.")
    print("Data type:", type(value))

else:
    print("You entered a string.")
    print("Data type:", type(value))