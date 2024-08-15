import time

print("Please insert your card")
time.sleep(2)

password = 1234
balance = 5000
transaction_history = []

try:
    pin = int(input("Enter your ATM Pin: "))
except ValueError:
    print("Invalid input. Please enter a numeric PIN.")
    exit()

if pin == password:
    while True:
        print("""
        1 == Balance 
        2 == Withdrawal Amount 
        3 == Deposit Balance 
        4 == Change Pin
        5 == Transaction History
        6 == Exit
        """)
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue

        if option == 1:
            print(f"Your current balance is {balance}")
            print("==================================")
        elif option == 2:
            try:
                withdraw_amount = int(input("Please enter withdrawal amount: "))
                if withdraw_amount > balance:
                    print("Insufficient balance")
                else:
                    balance -= withdraw_amount
                    transaction_history.append(f"Withdrawal: {withdraw_amount}")
                    print(f"{withdraw_amount} is debited from your account")
                    print("==============================================")
                    print(f"Your updated balance is {balance}")
                    print("==================================")
            except ValueError:
                print("Please enter a valid amount")
        elif option == 3:
            try:
                deposit_amount = int(input("Please enter deposit amount: "))
                balance += deposit_amount
                transaction_history.append(f"Deposit: {deposit_amount}")
                print(f"{deposit_amount} is credited to your account")
                print("============================================")
                print(f"Your updated balance is {balance}")
                print("==================================")
            except ValueError:
                print("Please enter a valid amount")
        elif option == 4:
            try:
                new_pin = int(input("Enter your new PIN: "))
                confirm_new_pin = int(input("Confirm your new PIN: "))
                if new_pin == confirm_new_pin:
                    password = new_pin
                    print("PIN successfully changed!")
                else:
                    print("PINs do not match. Try again.")
            except ValueError:
                print("Please enter a valid numeric PIN")
        elif option == 5:
            print("Transaction History:")
            if transaction_history:
                for transaction in transaction_history:
                    print(transaction)
            else:
                print("No transactions yet.")
            print("==================================")
        elif option == 6:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Please enter a valid option")
else:
    print("Wrong PIN. Please try again.")
