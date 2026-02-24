#prime no.

n = int(input("enter a number:"))

if n < 2:
    print(n, "is not a prime number.")
elif n == 2:
    print(n, "is a prime number.")
else:
    isprime = True

    for i in range(2, n):
        if n % i == 0:
            isprime = False
            break
    if isprime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")

#range of prime numbers

start = int(input("enter the range of start:"))
end = int(input("enter the range of end:"))
print("prime numbers between", start, "and", end, "are:")
for n in range(start, end + 1):
    if n >= 2:
        isprime = True

        for i in range(2, n):
            if n % i == 0:
                isprime = False
                break
        if isprime:
            print(n)