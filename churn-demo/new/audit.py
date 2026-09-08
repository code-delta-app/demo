# Audit trail for the ledger demo — new in this version.
class Audit:
    def __init__(self):
        self.events = []

    def record(self, kind, amount):
        self.events.append((kind, amount))
        return len(self.events)

    def total(self, kind):
        return sum(a for k, a in self.events if k == kind)
