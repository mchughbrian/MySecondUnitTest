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
        #need to fill this in

    def test_check_balance(self):
        #need to fill this in


if __name__ == '__main__':
    unittest.main()
