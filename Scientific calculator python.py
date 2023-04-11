import math

def scientific_calculator():
    print("Welcome to the scientific calculator!")
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square root")
    print("7. Factorial")
    print("8. Trigonometry")
    print("9. Logarithm")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result: ", num1 + num2)

    elif choice == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result: ", num1 - num2)

    elif choice == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result: ", num1 * num2)

    elif choice == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("Error: division by zero")
        else:
            print("Result: ", num1 / num2)

    elif choice == 5:
        num1 = float(input("Enter the base: "))
        num2 = float(input("Enter the exponent: "))
        print("Result: ", num1 ** num2)

    elif choice == 6:
        num = float(input("Enter a number: "))
        if num < 0:
            print("Error: cannot take square root of negative number")
        else:
            print("Result: ", math.sqrt(num))

    elif choice == 7:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Error: cannot take factorial of negative number")
        else:
            print("Result: ", math.factorial(num))

    elif choice == 8:
        print("Select a trigonometric function:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        trig_choice = int(input("Enter your choice: "))
        if trig_choice == 1:
            num = float(input("Enter an angle (in degrees): "))
            print("Result: ", math.sin(math.radians(num)))
        elif trig_choice == 2:
            num = float(input("Enter an angle (in degrees): "))
            print("Result: ", math.cos(math.radians(num)))
        elif trig_choice == 3:
            num = float(input("Enter an angle (in degrees): "))
            print("Result: ", math.tan(math.radians(num)))
        else:
            print("Invalid input, please try again.")

    elif choice == 9:
        num1 = float(input("Enter the number: "))
        base = float(input("Enter the base: "))
        print("Result: ", math.log(num1, base))

    elif choice == 10:
        print("Goodbye!")
        return

    else:
        print("Invalid input, please try again.")

    scientific_calculator()

scientific_calculator()
