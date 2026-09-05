class Ledger:
    def __init__(self, name):
        self.name = name
        self.previous_name = ""
        self.balance = 0.0
        self.limit = 0.0
        self.interest_paid = 0.0
        self.transfers = 0
        self.pending_holds = 0
        self.cleared_items = 0
        self.flagged_items = 0
        self.disputed_items = 0
        self.entries = []
        self.summary = {}

    def post(self, status, amount):
        self.entries.append((status, amount))
        self.balance = self.balance + amount
        self.log("posted")

    def credit(self, amount):
        self.post("posted", amount)
        self.cleared_items += 1

    def debit(self, amount):
        self.post("posted", -amount)
        self.cleared_items += 1

    def hold(self, amount):
        self.post("pending", amount)
        self.pending_holds += 1

    def dispute(self, amount):
        self.post("disputed", amount)
        self.disputed_items += 1
        self.flagged_items += 1

    def transfer(self, to, amount):
        self.debit(amount)
        to.credit(amount)
        self.transfers += 1

    def apply_interest(self, rate):
        interest = self.balance * rate
        self.post("posted", interest)
        self.interest_paid += interest

    def flag_large(self, threshold):
        n = 0
        for status, amount in self.entries:
            if abs(amount) > threshold:
                n += 1
        self.flagged_items += n
        return n

    def largest_entry(self):
        best = 0.0
        for status, amount in self.entries:
            if abs(amount) > abs(best):
                best = amount
        return best

    def statement_line(self, i):
        status, amount = self.entries[i]
        return "%s:%.2f" % (status, amount)

    def rename(self, new_name):
        self.previous_name = self.name
        self.name = new_name
        self.log("renamed")

    def net_flow(self):
        return self.sum_signed(+1) - self.sum_signed(-1)

    def reset(self):
        self.entries = []
        self.summary = {}
        self.balance = 0.0
        self.log("reset")

    def sum_signed(self, sign):
        total = 0.0
        for status, amount in self.entries:
            if (amount >= 0) == (sign > 0):
                total += abs(amount)
        return total

    def count_status(self, wanted):
        n = 0
        for status, amount in self.entries:
            if status == wanted:
                n += 1
        return n

    def set_limit(self, limit):
        self.limit = limit
        self.log("limit changed")

    def over_limit(self):
        return self.balance < -self.limit

    def entry_count(self):
        return len(self.entries)

    def summary_value(self, key):
        return self.summary.get(key, 0.0)

    def reconcile(self):
        opening = self.balance
        credits = self.sum_signed(+1)
        debits = self.sum_signed(-1)
        closing = opening + credits - debits
        drift = closing - self.balance
        posted = self.count_status("posted")
        pending = self.count_status("pending")
        disputed = self.count_status("disputed")
        total = posted + pending + disputed
        average = (credits + debits) / total if total > 0 else 0.0
        self.summary["opening"] = opening
        self.summary["credits"] = credits
        self.summary["debits"] = debits
        self.summary["closing"] = closing
        self.summary["drift"] = drift
        self.summary["posted"] = posted
        self.summary["pending"] = pending
        self.summary["disputed"] = disputed
        self.summary["average"] = average
        self.balance = closing

    def log(self, m):
        pass
