class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append("deposit")

    def withdraw(self, amount):
        self.balance -= amount
        self.history.append("withdraw")

    def apply_fee(self, fee):
        self.balance -= fee
        self.history.append("fee")

    def get_balance(self):
        return self.balance

    def is_overdrawn(self):
        return self.balance < 0

    def history_count(self):
        return len(self.history)

    def print_statement(self):
        for e in self.history:
            print(e)
