import os
import unittest

from banking_system import Bank
from account import InsufficientFundsError


class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.bank.create_account('Jayden', 100.0)
        self.bank.create_account('Michael', 50.0)

    def test_deposit_withdraw(self):
        self.bank.deposit('Jayden', 100.0)
        self.assertEqual(self.bank.accounts['Jayden'].balance, 200.0)
        self.bank.withdraw('Michael', 20.0)
        self.assertEqual(self.bank.accounts['Michael'].balance, 30.0)
        with self.assertRaises(ValueError):
            self.bank.deposit('Jayden', -100.0)
        with self.assertRaises(ValueError):
            self.bank.withdraw('Michael', -20.0)

    def test_overdraft(self):
        with self.assertRaises(InsufficientFundsError):
            self.bank.withdraw('Jayden', 200.0)

    def test_transfer(self):
        self.bank.transfer('Jayden', 'Michael', 50.0)
        self.assertEqual(self.bank.accounts['Jayden'].balance, 50.0)
        self.assertEqual(self.bank.accounts['Michael'].balance, 100.0)
        with self.assertRaises(KeyError):
            self.bank.transfer('Jayden', 'Yulia', 50.0)
        with self.assertRaises(ValueError):
            self.bank.transfer('Jayden', 'Jayden', 50.0)
        with self.assertRaises(ValueError):
            self.bank.transfer('Jayden', 'Michael', -50.0)
        with self.assertRaises(InsufficientFundsError):
            self.bank.transfer('Jayden', 'Michael', 100.0)

    def test_csv_save_and_load(self):
        filename = 'test_accounts.csv'
        try:
            self.bank.save_to_csv(filename)
            # create a new bank and load
            new_bank = Bank()
            new_bank.load_from_csv(filename)
            self.assertIn('Jayden', new_bank.accounts)
            self.assertIn('Michael', new_bank.accounts)
            self.assertEqual(new_bank.accounts['Jayden'].balance, 100.0)
            self.assertEqual(new_bank.accounts['Michael'].balance, 50.0)
        finally:
            if os.path.exists(filename):
                os.remove(filename)


if __name__ == '__main__':
    unittest.main()

