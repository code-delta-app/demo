class Account {
  constructor(owner, balance) {
    this.owner = owner;
    this.balance = balance;
    this.history = [];
  }

  deposit(amount) {
    this.balance += amount;
    this.history.push("deposit");
  }

  withdraw(amount) {
    this.balance -= amount;
    this.history.push("withdraw");
  }

  applyFee(fee) {
    this.balance -= fee;
    this.history.push("fee");
  }

  getBalance() {
    return this.balance;
  }

  isOverdrawn() {
    return this.balance < 0;
  }

  historyCount() {
    return this.history.length;
  }

  printStatement() {
    for (const e of this.history) {
      console.log(e);
    }
  }
}
