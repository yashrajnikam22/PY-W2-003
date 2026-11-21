from decimal import Decimal

class Account:
    def __init__(self, account_no, customer_id, balance = 0):
        self.account_no = account_no
        self.customer_id = customer_id
        self.balance = Decimal(str(balance))
        self.status = "Active"

        if not self.balance.is_canonical() or self.balance < 0:
            raise ValueError("Initial balance must be a valid non-negative amount.")

    def deposite(self,amount):
        amount = Decimal(str(self.balance))

        if not amount.is_finite or amount <= 0:
            raise ValueError("Deposite amount must be positive")

        if self.status != "Active":
            raise ValueError("Account is not active!")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        amount = Decimal(str(self.balance))

        if not amount.is_finite or amount <= 0:
            raise ValueError("Deposite amount must be positive")
        
        if self.status != "Active":
            raise ValueError("Account is not active!")

        if amount > self.balance:
            raise ValueError("Insufficient balance!")

        self.balance -= amount

    def display_balance(self):
        print(f"Account Balance: ₹{self.balance}")

