class Account {
  owner: string;
  balance: number;
  history: string[];

  constructor(owner: string, balance: number) {
    this.owner = owner;
    this.balance = balance;
    this.history = [];
  }

  deposit(amount: number): void {
    this.balance += amount;
    this.history.push("deposit");
  }

  withdraw(amount: number): void {
    this.balance -= amount;
    this.history.push("withdraw");
  }

  applyFee(fee: number): void {
    this.balance -= fee;
    this.history.push("fee");
  }

  getBalance(): number {
    return this.balance;
  }

  isOverdrawn(): boolean {
    return this.balance < 0;
  }

  historyCount(): number {
    return this.history.length;
  }

  printStatement(): void {
    for (const e of this.history) {
      console.log(e);
    }
  }
}
