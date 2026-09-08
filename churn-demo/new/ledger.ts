interface Entry { status: string; amount: number; }

class Ledger {
    name: string;
    previousName: string;
    balance: number;
    limit: number;
    interestPaid: number;
    transfers: number;
    pendingHolds: number;
    clearedItems: number;
    flaggedItems: number;
    disputedItems: number;
    entries: Entry[];
    summary: Map<string, number>;
    lastLog: string;
    constructor(name: string) {
        this.name = name;
        this.previousName = "";
        this.balance = 0;
        this.limit = 0;
        this.interestPaid = 0;
        this.transfers = 0;
        this.pendingHolds = 0;
        this.clearedItems = 0;
        this.flaggedItems = 0;
        this.disputedItems = 0;
        this.entries = [];
        this.summary = new Map();
        this.lastLog = "";
    }

    log(m: string): void {
        this.lastLog = m;
    }

    post(status: string, amount: number): void {
        this.entries.push({ status, amount });
        this.balance = this.balance + amount;
        this.log("posted");
    }

    credit(amount: number): void {
        this.post("posted", amount);
        this.clearedItems += 1;
    }

    debit(amount: number): void {
        this.post("posted", -amount);
        this.clearedItems += 1;
    }

    hold(amount: number): void {
        this.post("pending", amount);
        this.pendingHolds += 1;
    }

    dispute(amount: number): void {
        this.post("disputed", amount);
        this.disputedItems += 1;
        this.flaggedItems += 1;
    }

    transfer(to: Ledger, amount: number): void {
        this.debit(amount);
        to.credit(amount);
        this.transfers += 1;
    }

    applyInterest(rate: number): void {
        const interest = this.balance * rate;
        this.post("posted", interest);
        this.interestPaid += interest;
    }

    flagLarge(threshold: number): number {
        let n = 0;
        for (const e of this.entries) {
            if (Math.abs(e.amount) > threshold) n += 1;
        }
        this.flaggedItems += n;
        return n;
    }

    largestEntry(): number {
        let best = 0;
        for (const e of this.entries) {
            if (Math.abs(e.amount) > Math.abs(best)) best = e.amount;
        }
        return best;
    }

    statementLine(i: number): string {
        const e = this.entries[i];
        return e.status + ":" + String(e.amount);
    }

    rename(newName: string): void {
        this.previousName = this.name;
        this.name = newName;
        this.log("renamed");
    }

    netFlow(): number {
        return this.sumSigned(+1) - this.sumSigned(-1);
    }

    reset(): void {
        this.entries = [];
        this.summary = new Map();
        this.balance = 0;
        this.log("reset");
    }

    sumSigned(sign: number): number {
        let sum = 0;
        for (const e of this.entries) {
            if ((e.amount >= 0) === (sign > 0)) sum += Math.abs(e.amount);
        }
        return sum;
    }

    countStatus(status: string): number {
        let n = 0;
        for (const e of this.entries) {
            if (e.status === status) n += 1;
        }
        return n;
    }

    setLimit(limit: number): void {
        this.limit = limit;
        this.log("limit changed");
    }

    overLimit(): boolean {
        return this.balance < -this.limit;
    }

    entryCount(): number {
        return this.entries.length;
    }

    summaryValue(key: string): number {
        return this.summary.get(key) ?? 0;
    }

    reconcile(): void {
        const opening = this.balance;
        const credits = this.sumSigned(+1);
        const debits = this.sumSigned(-1);
        const closing = opening + credits - debits;
        const drift = closing - this.balance;
        const posted = this.countStatus("posted");
        const pending = this.countStatus("pending");
        const disputed = this.countStatus("disputed");
        const total = posted + pending + disputed;
        const average = total > 0 ? (credits + debits) / total : 0;
        this.summary.set("opening", opening);
        this.summary.set("credits", credits);
        this.summary.set("debits", debits);
        this.summary.set("closing", closing);
        this.summary.set("drift", drift);
        this.summary.set("posted", posted);
        this.summary.set("pending", pending);
        this.summary.set("disputed", disputed);
        this.summary.set("average", average);
        this.balance = closing + this.interestPaid;
    }

    resetCounters(): void { this.pendingHolds = 0; this.clearedItems = 0; this.flaggedItems = 0; this.disputedItems = 0; }
}

export { Ledger };
