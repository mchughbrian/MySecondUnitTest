import unittest
from main import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        #This means that each test case starts with
        # A fresh BankAccount object with a balance of 100
        self.account = BankAccount("Test Account", 100)

    def test_initialization(self):
        # Test that a ValueError is raised when the initial balance is not a number
        with self.assertRaises(ValueError):
            BankAccount("Bad Account", "not a number")

        # Test that a ValueError is raised when the initial balance is negative
        with self.assertRaises(ValueError):
            BankAccount("Bad Account", -100)

    def test_deposit(self):
        # Test that depositing a positive amount increases the balance
        self.account.deposit(50)
        self.assertEqual(self.account.check_balance(), 150, "Failed on depositing a positive amount.")

        # Test that depositing zero does not change the balance
        self.account.deposit(0)
        self.assertEqual(self.account.check_balance(), 150, "Failed on depositing zero.")

        # Test that depositing a negative amount raises a ValueError
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_withdraw(self):
        # Test that withdrawing a positive amount decreases the balance
        self.account.withdraw(50)
        self.assertEqual(self.account.check_balance(), 50, "Failed on withdrawing a positive amount.")

        # Test that withdrawing the entire balance sets the balance to zero
        self.account.withdraw(50)
        self.assertEqual(self.account.check_balance(), 0, "Failed on withdrawing the entire balance.")

        # Test that withdrawing a negative amount raises a ValueError
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)

        # Test that withdrawing an amount larger than the balance raises a ValueError
        with self.assertRaises(ValueError):
            self.account.withdraw(100)

    def test_check_balance(self):
        # Test that check_balance returns the correct balance
        self.assertEqual(self.account.check_balance(), 100, "Failed on initial balance check.")

        # Deposit some money and check the balance
        self.account.deposit(50)
        self.assertEqual(self.account.check_balance(), 150, "Failed on balance check after deposit.")

        # Withdraw some money and check the balance
        self.account.withdraw(50)
        self.assertEqual(self.account.check_balance(), 100, "Failed on balance check after withdrawal.")


if __name__ == '__main__':
    unittest.main()
