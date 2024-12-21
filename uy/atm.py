###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
# initial 4-digit PIN code
pinc = 1111
while True:
    
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    pin = int(input("whats your pin: ")) 
    choice = input("Choose an option (1-4): ")
    print()
    if pin == pinc:
            if choice == '1':
            print(f"Your current balance is: €{balance}")
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            balance += amount
            print(f"€{amount} has been deposited. New balance: €{balance}")
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"€{amount} has been withdrawn. New balance: €{balance}")
            else:
                print("Insufficient balance.")
        elif choice == '4':
            print("Exiting... Thank you for using the ATM!")
            break  # Exit the loop
        else:
            print("Invalid option. Please try again.")
    else:
        break