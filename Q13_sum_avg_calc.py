#sum, avg, max, min

count = int(input("enter how many numbers:"))
sum = 0
max = None
min = None

for i in range(1, count + 1):
    num = float(input("enter number " + str(i) + ":"))
    sum += num
    if max is None or num > max:
        max = num
    if min is None or num < min:
        min = num

if count > 0:
    avg = sum / count
else:
    avg = 0

print("sum:", sum)
print("average:", avg)
print("max:", max)
print("min:", min)  
    