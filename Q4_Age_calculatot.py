#Age calculator

#input birh year
birth_year = int(input("Enter your birth year: "))
#input current year
current_year = int(input("Enter the current year: "))

#Age calcutation
age = current_year - birth_year

age_months = age * 12
age_day = age * 365
age_hours = age_day * 24
age_minutes = age_hours * 60

#output
print("current age in years: ", age)
print("current age months: ", age_months)
print("current age days: ", age_day)
print("current age in hours: ", age_hours)
print("current age minutes: ", age_minutes)