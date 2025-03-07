def calc():
    # Ask for the operator and keep asking until it's valid
    while True:
        operator = input("What operator would you like to use? (+ - * /): ")
        if operator in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid operator! Please enter one of the following: +, -, *, /")

    # Ask for numbers, validate they are valid floats
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Perform the calculation
    result = 0

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero."

    return result


def calculator():
    while True:
        result = calc()
        print("Result:", result)

        # Ask if the user wants to perform another calculation
        again = input("Would you like to make another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break


calculator()
