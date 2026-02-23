#multiplication table for number

number = int(input("Enter number: "))
end_range = int(input("Enter range (end): "))

print("\nMultiplication Table of", number)

# using for loop
for i in range(1, end_range + 1):
    result = number * i
    print(number, "x", i, "=", result)