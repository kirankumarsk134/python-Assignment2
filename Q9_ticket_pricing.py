#ticket pricing

# taking inputs
age = int(input("Enter age: "))
day = input("Enter day of the week: ")
num_tickets = int(input("Enter number of tickets: "))

#ticket price using age
if age < 3:
    price = 0
    category = "Free"
elif age >= 3 and age <= 12:
    price = 150
    category = "Child"
elif age >= 13 and age <= 59:
    price = 300
    category = "Adult"
else:
    price = 200
    category = "Senior"

#base price calculation
base_price = price * num_tickets

#discount based on day
day = day.lower()

if day == "friday" or day == "saturday" or day == "sunday":
    discount = base_price * 0.20
    discount_message = "20% discount applied"
else:
    discount = 0
    discount_message = "No discount"

#price after discount
final_price = base_price - discount

# displaying output
print("\nTicket pricing details:")
print("category:", category)
print("price per ticket: ₹", price)
print("Number of tickets:", num_tickets)
print("baseprice: ₹", base_price)
print("Ddiscount:", discount_message)
print("dicount amount: ₹", round(discount, 2))
print("price after discount: ₹", round(final_price, 2))
print("Total amount to pay: ₹", round(final_price, 2))