# number system functions with menu

# 1. factorial function
def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

# 2. prime check function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 3. fibonacci function (nth term)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a = 0
    b = 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b

# 4. sum of digits
def sum_of_digits(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n = n // 10
    return total

# 5. reverse number
def reverse_number(n):
    rev = 0
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    while n > 0:
        rev = rev * 10 + (n % 10)
        n = n // 10
    return rev * sign

# 6. armstrong number check
def is_armstrong(n):
    temp = abs(n)
    power = len(str(temp))
    sum_val = 0
    t = temp
    while t > 0:
        digit = t % 10
        sum_val += digit ** power
        t = t // 10
    if sum_val == temp:
        return True
    else:
        return False

# 7. gcd function
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

# 8. lcm function
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

# 9. perfect number check
def is_perfect_number(n):
    if n <= 1:
        return False
    sum_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_div += i
    if sum_div == n:
        return True
    else:
        return False

# 10. menu function
def math_menu():
    while True:
        print("\n=== NUMBER SYSTEM MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci (nth term)")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter a number: "))
            print("Factorial:", factorial(n))

        elif choice == "2":
            n = int(input("Enter a number: "))
            if is_prime(n):
                print("Prime Number")
            else:
                print("Not a Prime Number")

        elif choice == "3":
            n = int(input("Enter n: "))
            print("Fibonacci term:", fibonacci(n))

        elif choice == "4":
            n = int(input("Enter a number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == "5":
            n = int(input("Enter a number: "))
            print("Reversed number:", reverse_number(n))

        elif choice == "6":
            n = int(input("Enter a number: "))
            if is_armstrong(n):
                print("Armstrong Number")
            else:
                print("Not an Armstrong Number")

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == "9":
            n = int(input("Enter a number: "))
            if is_perfect_number(n):
                print("Perfect Number")
            else:
                print("Not a Perfect Number")

        elif choice == "10":
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

# calling menu
math_menu()