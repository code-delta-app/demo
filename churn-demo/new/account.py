class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.min_balance = 0.0
        self.history = []

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.history.append("DEPOSIT")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.history.append("WITHDRAW")

    def apply_fee(self, fee):
        self.balance = self.balance - fee
        self.history.append("FEE")

    def get_balance(self):
        return self.balance

    def is_overdrawn(self):
        return self.balance < self.min_balance

    def history_count(self):
        return len(self.history)

    def apply_interest(self, rate):
        self.balance = self.balance + self.balance * rate
        self.history.append("INTEREST")
