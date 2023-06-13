# This is a script for a BankAccount. We will create a unit test off this script

class BankAccount:
    # Initialize a BankAccount object with a name and an initial balance.
    # The initial balance defaults to 0.0 if not provided.
    def __init__(self, name, initial_balance=0.0):
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
