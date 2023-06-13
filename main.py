# This is a script for a BankAccount. We will create a unit test off this script

class BankAccount:
    # Initialize a BankAccount object with a name and an initial balance.
    # The initial balance defaults to 0.0 if not provided.
    def __init__(self, name, initial_balance=0.0):
        #need to handle non-numeric inputs
        if not isinstance(initial_balance, (int, float)):
            raise ValueError("Initial balance must be a number.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.name = name  # The name associated with the BankAccount
        self.balance = initial_balance  # The current balance of the BankAccount


    # Deposit the specified amount into the BankAccount.
    # If the amount is negative, raise a ValueError.
    # Return the new balance.
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    # Withdraw the specified amount from the BankAccount.
    # If the amount is negative, raise a ValueError.
    # If the BankAccount does not have enough funds to cover the withdrawal, raise a ValueError.
    # Return the new balance.
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    # Return the current balance of the BankAccount.
    def check_balance(self):
        return self.balance

# Working through a few examples of class working
# Create a BankAccount object with the name "John's account" and an initial balance of 100
account_john = BankAccount("John's account", 100)

# Deposit 50 into the account
account_john.deposit(50)
print(account_john.check_balance())  # Outputs: 150

account_mike = BankAccount("Mike's Account", 200)
# Deposit 50 into the account
account_mike.deposit(50)
print(account_mike.check_balance())  # Outputs: 250

# Withdraw 20 from the account
account_john.withdraw(20)
print(account_john.check_balance())  # Outputs: 130

# Attempt to withdraw 250 from Jane's account
# This will raise a ValueError because there are insufficient funds
try:
    account_john.withdraw(250)
except ValueError as e:
    print(e)  # Outputs: Insufficient funds.


