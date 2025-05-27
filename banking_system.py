import csv
from typing import Dict

from account import Account, InsufficientFundsError


class Bank:
    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def create_account(self, name: str, starting_balance: float = 0.0):
        if name in self.accounts:
            raise ValueError(f'Account with name "{name}" already exists')
        new_account = Account(name, starting_balance)
        self.accounts[name] = new_account

    def _get_account(self, name: str) -> Account:
        if name not in self.accounts:
            raise KeyError(f'Account with name "{name}" does not exist')
        return self.accounts[name]

    def deposit(self, name: str, amount: float):
        self._get_account(name).deposit(amount)

    def withdraw(self, name: str, amount: float):
        self._get_account(name).withdraw(amount)

    def transfer(self, from_name: str, to_name: str, amount: float):
        if from_name not in self.accounts or to_name not in self.accounts:
            raise KeyError('Only transfer in the same banking system')
        elif from_name == to_name:
            raise ValueError('Cannot transfer to the same account')
        elif amount <= 0:
            raise ValueError(f'Amount must be positive')
        elif amount > self._get_account(from_name).balance:
            raise InsufficientFundsError(from_name, amount, self._get_account(from_name).balance)

        self._get_account(from_name).withdraw(amount)
        self._get_account(to_name).deposit(amount)

    def save_to_csv(self, filename: str):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'Balance'])
            for account in self.accounts.values():
                writer.writerow([account.name, f'{account.balance:.2f}'])

    def load_from_csv(self, filename: str):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            self.accounts.clear()
            for row in reader:
                name = row['Name']
                balance = float(row['Balance'])
                self.create_account(name, balance)
