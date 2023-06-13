# Working through a few examples of class working
# Create a BankAccount object with the name "John's account" and an initial balance of 100
from main import BankAccount

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


