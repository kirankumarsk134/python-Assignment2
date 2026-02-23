#ATM simulator

balance = 100000

while True:
    print("\nATM Simulator")
    print("1. Check bal")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Current balance: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance = balance + amount
            print("Deposit successful")
            print("New balance: ₹", balance)
        else:
            print("Invalid deposit amount!")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        
        if amount > balance:
            print("Insufficient balance")
        elif balance - amount < 500:
            print("Withdrawal denied! Minimum balance of ₹500 must remain.")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            balance = balance - amount
            print("Withdrawal successful")
            print("New balance: ₹", balance)

    elif choice == "4":
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice!")