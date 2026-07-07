def calculator():
    print("Welcome to calculator!")
    print("Operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero")
                    continue
                result = num1 / num2
            else:
                print("Error: Invalid operator")
                continue

            print(f"Result: {num1} {op} {num2} = {result}")

        except ValueError:
            print("Error: Please enter valid numbers")

        again = input("\nCalculate again? (y/n): ")
        if again.lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()