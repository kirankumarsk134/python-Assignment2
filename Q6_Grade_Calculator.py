#grade calculator 

#input for 5 subs
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))
sub4 = float(input("Enter marks for subject 4: "))
sub5 = float(input("Enter marks for subject 5: "))

#marks
print("\nMarks obtained:")
print("Subject 1: ", sub1)
print("Subject 2: ", sub2)
print("Subject 3: ", sub3)  
print("Subject 4: ", sub4)
print("Subject 5: ", sub5)

Total_marks= sub1 + sub2 + sub3 + sub4 + sub5
average = Total_marks / 5 

#grade calculation
if average >= 90:
    grade = "A+ (Outstanding)"
elif average >= 80:
    grade = "A (Excellent)"
elif average >= 70:
    grade = "B (Good)"
elif average >= 60:    
    grade = "C (Average)"
elif average >= 50:   
    grade = "D(pass)"
else:
    grade = "F (Fail)"


#pass/fail
if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
    result = "Pass"
else:
    result = "Fail"

#final output
print("Result ")
print("Total marks: ", Total_marks)
print("Average marks: ", average)      
print("Grade: ", grade)
print("Final Result: ", result)

