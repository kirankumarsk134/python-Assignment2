#calculator 

# function for addition
def add(a, b):
    return a + b

# function for subtraction
def subtract(a, b):
    return a - b

# function for multiplication
def multiply(a, b):
    return a * b

# function for division
def divide(a, b):
    if b == 0:
        return "Cant divide by zero"
    else:
        return a / b

# function for modulus
def modulus(a, b):
    if b == 0:
        return "Cant perform modulus with zero"
    else:
        return a % b

# function for power
def power(a, b):
    return a ** b

# main calculator function with menu
def calculator():
    while True:
        print("CALCULATOR MENu")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Exiting calculator...")
            break

        # taking inputs
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        # calling appropriate function
        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
        elif choice == "5":
            result = modulus(a, b)
        elif choice == "6":
            result = power(a, b)
        else:
            print("Invalid choice!")
            continue

        print("Result:", result)

#main function call
calculator()