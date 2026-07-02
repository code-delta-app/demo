class Account {
  constructor(owner, balance) {
    this.owner = owner;
    this.balance = balance;
    this.minBalance = 0;
    this.history = [];
  }

  deposit(amount) {
    this.balance = this.balance + amount;
    this.history.push("DEPOSIT");
  }

  withdraw(amount) {
    this.balance = this.balance - amount;
    this.history.push("WITHDRAW");
  }

  applyFee(fee) {
    this.balance = this.balance - fee;
    this.history.push("FEE");
  }

  getBalance() {
    return this.balance;
  }

  isOverdrawn() {
    return this.balance < this.minBalance;
  }

  historyCount() {
    return this.history.length;
  }

  applyInterest(rate) {
    this.balance = this.balance + this.balance * rate;
    this.history.push("INTEREST");
  }
}
