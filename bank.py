class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def deposit(self, amount):
        self.balance += amount
        return amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return "Insufficient balance"
    def check_balance(self):
        print(f"Current balance: {self.balance}")
    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Current Balance: {self.balance}")
# Example usage of the BankAccount class
account = BankAccount("1234567890", 1000.0, "2023-01-01", "John Doe")

# Deposit money into the account
deposited_amount = account.deposit(500.0)
print(f"Deposited Amount: {deposited_amount}")

# Attempt to withdraw money (insufficient balance)
withdrawn_amount = account.withdraw(2000.0)
print(f"Withdrawn Amount: {withdrawn_amount}")

