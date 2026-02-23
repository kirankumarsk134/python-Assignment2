#Simple Calculator

#taking user input
n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))

add = n1 + n2
sub = n1 - n2
mul = n1 * n2
expo = n1 ** n2

#checking that the 2nd no. is not zero, if it is zero the ans of division and moduulus is not defined.
if n2 == 0:
    print("division not possible")
    print("modulus not possible")
else:
    div = n1 / n2
    mod = n1 % n2
    print( n1, "+", n2, "=", add)
    print(n1, "-", n2, "=", sub)
    print(n1, "*", n2, "=", mul)
    print(n1, "/", n2, "=", div)
    print(n1, "and", n2, "=", mod)
    print(n1, "**", n2, "=", expo)