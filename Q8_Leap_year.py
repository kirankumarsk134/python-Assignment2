#Leap year checker

year = int(input("Enter a year: "))

# checking leap year condition
if year % 4 == 0:
    if year % 100 != 0:
        print(year, "is Leap Year")
        (print("because divisible by 4 but not by 100"))
    else:
        if year % 400 == 0:
            print(year, "is Leap Year")
            (print("because divisible by 100 and also by 400"))
        else:
            print(year, "is NOT a Leap Year")
            print("because divisible by 100 but not by 400")
else:
    print(year, "is NOT a Leap Year")
    print("because not divisible by 4")