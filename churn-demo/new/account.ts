class Account {
  owner: string;
  balance: number;
  minBalance: number;
  history: string[];

  constructor(owner: string, balance: number) {
    this.owner = owner;
    this.balance = balance;
    this.minBalance = 0;
    this.history = [];
  }

  deposit(amount: number): void {
    this.balance = this.balance + amount;
    this.history.push("DEPOSIT");
  }

  withdraw(amount: number): void {
    this.balance = this.balance - amount;
    this.history.push("WITHDRAW");
  }

  applyFee(fee: number): void {
    this.balance = this.balance - fee;
    this.history.push("FEE");
  }

  getBalance(): number {
    return this.balance;
  }

  isOverdrawn(): boolean {
    return this.balance < this.minBalance;
  }

  historyCount(): number {
    return this.history.length;
  }

  applyInterest(rate: number): void {
    this.balance = this.balance + this.balance * rate;
    this.history.push("INTEREST");
  }
}
