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
        #need to fill this in

    def test_withdraw(self):
        #need to fill this in

    def test_check_balance(self):
        #need to fill this in


if __name__ == '__main__':
    unittest.main()
