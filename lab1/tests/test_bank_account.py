import unittest
from lab1.src.bank_account import BankAccount

class TestEmail(unittest.TestCase):

    def setUp(self):
        self.bank_account = BankAccount(0.0)

    def tearDown(self):
        pass

    def test_balance_positive(self):
        self.assertEqual(self.bank_account.get_balance(),0)

    def test_balance_negative(self):
        self.assertNotEqual(self.bank_account.get_balance(),8)

    def test_deposit_positive(self):
        self.bank_account.deposit(200)
        self.assertEqual(self.bank_account.get_balance(),200)

    def test_deposit_negative(self):
        self.bank_account.deposit(200)
        self.assertNotEqual(self.bank_account.get_balance(),2500)

    def test_withdraw_positive(self):
        self.bank_account.deposit(200)
        self.bank_account.withdraw(50)
        self.assertEqual(self.bank_account.get_balance(),150)

    def test_withdraw_negative(self):
        self.bank_account.deposit(200)
        self.bank_account.withdraw(150)
        self.assertNotEqual(self.bank_account.get_balance(),150)

    def test_withdraw_error(self):
        with self.assertRaises(ValueError):
             self.bank_account.withdraw(50)


if __name__ =="__main__":
    unittest.main()