#Bill Splitter

#user inputs
bill = float(input("total bill(input): "))
people = int(input("Number of people: "))
tax = float(input("Tax %: "))
tip = float(input("Tip %: "))

# subtotal=original bill
subtotal = bill

#tax amount
tax_amount = (tax * subtotal) / 100

#bill+ tax
aft_tax = subtotal + tax_amount

#calculating tip amount
tip_amount = (tip * aft_tax) / 100

#final total bill
total = aft_tax + tip_amount

#calculating amount per person
if people > 0:
    per_person = total / people
else:
    per_person = 0
    print("Invalid no. of people!")

# displaying formatted output
print("\nBILL BREAKDOWN")
print("Subtotal: rs{:.2f}".format(subtotal))
print("Tax ({}%): rs{:.2f}".format(tax, tax_amount))
print("After tax: rs{:.2f}".format(aft_tax))
print("Tip ({}%): rs{:.2f}".format(tip, tip_amount))
print("Total: rs{:.2f}".format(total))
print("Per person: rs{:.2f}".format(per_person))