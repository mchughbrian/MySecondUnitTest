import unittest
from main import BankAccount




class TestBankAccount(unittest.TestCase):

    def setUp(self):
        #This means that each test case starts with
        # A fresh BankAccount object with a balance of 100
        self.account = BankAccount("Test Account", 100)

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
