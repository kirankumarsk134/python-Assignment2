# palindrome checker

n = input("enter string or no.")
orginal = n
n = n.lower()

reveresed = ""
for ch in n:
    reveresed = ch + reveresed

print("original:", orginal)
print("reversed:", reveresed)

if n == reveresed:
    print("it is a palindrome.")
else:
    print("it is not a palindrome.")
    