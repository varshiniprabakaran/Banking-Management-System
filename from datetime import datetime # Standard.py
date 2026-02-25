from datetime import datetime   # Standard Python library

accounts = {}

def get_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# ---------------- CREATE ACCOUNT ----------------
def create_account():
    print("\n--- Create Account ---")

    acc_no = input("Enter 10-digit account number: ")
    if not acc_no.isdigit() or len(acc_no) != 10:
        print("Invalid account number! Must be exactly 10 digits.")
        return

    if acc_no in accounts:
        print("Account already exists!")
        return

    pin = input("Set 4-digit PIN: ")
    if not pin.isdigit() or len(pin) != 4:
        print("Invalid PIN! Must be exactly 4 digits.")
        return

    name = input("Enter account holder name: ")
    balance = int(input("Enter initial balance: "))

    accounts[acc_no] = {
        "name": name,
        "pin": pin,
        "balance": balance,
        "history": [
            f"Account created on {get_time()} | Balance: {balance}"
        ]
    }

    print("Account created successfully!")


# ---------------- PIN VALIDATION (NEW FEATURE) ----------------
def pin_validation_only():
    print("\n--- PIN Validation ---")
    acc_no = input("Enter account number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    pin = input("Enter PIN: ")

    if accounts[acc_no]["pin"] == pin:
        print("PIN validation successful ✅")
    else:
        print("Invalid PIN ❌")


# ---------------- DEPOSIT ----------------
def deposit_money():
    print("\n--- Deposit Money ---")
    acc_no = input("Enter account number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    amount = int(input("Enter deposit amount: "))
    accounts[acc_no]["balance"] += amount

    accounts[acc_no]["history"].append(
        f"Deposited {amount} on {get_time()} | Balance: {accounts[acc_no]['balance']}"
    )

    print("Deposit successful!")


# ---------------- WITHDRAW ----------------
def withdraw_money():
    print("\n--- Withdraw Money ---")
    acc_no = input("Enter account number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    amount = int(input("Enter withdrawal amount: "))

    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance!")
    else:
        accounts[acc_no]["balance"] -= amount

        accounts[acc_no]["history"].append(
            f"Withdrawn {amount} on {get_time()} | Balance: {accounts[acc_no]['balance']}"
        )

        print("Withdrawal successful!")


# ---------------- BALANCE ENQUIRY ----------------
def balance_enquiry():
    print("\n--- Balance Enquiry ---")
    acc_no = input("Enter account number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    print("Current Balance:", accounts[acc_no]["balance"])


# ---------------- TRANSACTION HISTORY ----------------
def transaction_history():
    print("\n--- Transaction History ---")
    acc_no = input("Enter account number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    print("\n----- STATEMENT -----")
    for item in accounts[acc_no]["history"]:
        print(item)

    print("---------------------")
    print("Final Available Balance:", accounts[acc_no]["balance"])


# ---------------- MAIN MENU ----------------
def main_menu():
    while True:
        print("\n===== BANKING MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Balance Enquiry")
        print("5. Transaction History")
        print("6. PIN Validation")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            balance_enquiry()
        elif choice == "5":
            transaction_history()
        elif choice == "6":
            pin_validation_only()
        elif choice == "7":
            print("Thank you for using Banking Management System.")
            break
        else:
            print("Invalid choice! Please try again.")


main_menu()
