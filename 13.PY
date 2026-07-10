class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f} successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account Balance: ${self.balance:.2f}")

    def __str__(self):
        return f"Account({self.account_number}, {self.account_holder}, Balance: ${self.balance:.2f})"


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, account_holder, initial_balance)
            print(f"Account created successfully for {account_holder}.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def perform_deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def perform_withdrawal(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def display_account_info(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")


def main():
    bank = BankSystem()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            acc_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(acc_num, acc_holder, initial_balance)

        elif choice == "2":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.perform_deposit(acc_num, amount)

        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.perform_withdrawal(acc_num, amount)

        elif choice == "4":
            acc_num = input("Enter account number: ")
            bank.display_account_info(acc_num)

        elif choice == "5":
            print("Exiting the banking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


    print(".")