class InsufficientFundsError(Exception):
    def __init__(self, name: str, amount: float, balance: float):
        self.name = name
        self.amount = amount
        self.balance = balance
        super().__init__(
            f"Account '{name}' has insufficient funds: "
            f"attempted to withdraw/transfer {amount}, but current balance is {balance}."
        )


class Account:
    def __init__(self, name: str, balance: float = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if self.balance == 0:
            raise ValueError("You don't have enough funds")
        elif amount < 0:
            raise ValueError("Withdraw amount must be positive")
        elif amount > self.balance:
            raise InsufficientFundsError(self.name, amount, self.balance)
        self.balance -= amount
