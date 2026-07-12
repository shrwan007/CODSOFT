def simple_calculator():
    print("--- Simple Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")
        return

    print("\nAvailable Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("\nChoose an operation (Enter 1/2/3/4 or +, -, *, /): ").strip()

    if choice in ['1', '+']:
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")

    elif choice in ['2', '-']:
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")

    elif choice in ['3', '*']:
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")

    elif choice in ['4', '/']:
        if num2 == 0:
            print("\nError: Division by zero is undefined and not allowed.")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")

    else:
        print("\nError: Invalid operation choice. Please try again.")

if __name__ == "__main__":
    simple_calculator()
