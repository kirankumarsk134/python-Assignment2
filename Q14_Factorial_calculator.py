#factorial of a number

n = int(input("enter a number:"))

if n < 0:
    print("factorial is not for negative ")
elif n == 0 or n == 1:
    print("factorial of", n, "is 1")

else:
    fact = 1
    print(str(n) + "! = ", end="")

    # loop for factorial calculation
    for i in range(n, 0, -1):
        fact = fact * i
        print(i, end="")
        
        if i != 1:
            print(" × ", end="")

    print(" = ", fact)