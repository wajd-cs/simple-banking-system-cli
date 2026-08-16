import datetime

class BankAccount:
    def __init__(self, account_number, owner_name):
        self.__balance = 0.0
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("You cannot deposit zero or negative amounts")
        else:
            self.__balance += amount
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.__transactions.append(f"Deposit: {amount} SAR at {now}")
            print("A sum of:", amount, "Riyals was deposited into your bank account on:", datetime.datetime.now())

    def withdraw(self, amount):
        if amount <= 0:
            print("You cannot withdraw zero or negative amounts")
        elif amount > self.__balance:
            print("You don't have enough money to withdraw")
        else:
            self.__balance -= amount
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.__transactions.append(f"Withdrawal: {amount} SAR at {now}")
            print("A sum of : ", amount, " Riyals was withdrawn from your bank account on : ", datetime.datetime.now())

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions.copy()

class SavingAccount(BankAccount):
    def get_balance(self):
        print("This is a saving account")
        return super().get_balance()

accounts = {}
while True:
    print("\n1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        owner_name = input("Enter your name: ").strip()
        account_number = input("Enter account number: ").strip()
        account_type = input("Choose account type (1: Normal, 2: Saving): ").strip()

        if account_number in accounts:
            print("Account number already exists")
            continue
        if account_type == "1":
            account_1 = BankAccount(account_number, owner_name)
        elif account_type == "2":
            account_1 = SavingAccount(account_number, owner_name)
        else:
            print("Invalid account type")
            continue

        accounts[account_number] = account_1
        print("Account created successfully!")

    elif choice == "2":
        account_number = input("Enter account number: ").strip()

        if account_number not in accounts:
            print("Account number does not exist")
            continue
        account = accounts[account_number]

        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Balance")
            print("4. Transactions History")
            print("5. Logout")

            choice = input("Enter your choice: ").strip()
            if choice == "1":
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                except ValueError:
                    print("Please enter a valid number")
            elif choice == "2":
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Please enter a valid number")
            elif choice == "3":
                print("Account balance:", account.get_balance(), "SAR")
            elif choice == "4":
                print("--- Transactions ---")
                logs = account.get_transactions()
                if not logs:
                    print("No transactions yet.")
                else:
                    for log in logs:
                        print(log)
            elif choice == "5":
                break
            else:
                print("Invalid choice")

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
