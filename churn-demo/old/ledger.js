class Ledger {
    constructor(name) {
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

    log(m) {
        this.lastLog = m;
    }

    reconcile() {
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
        this.balance = closing;
    }

    resetCounters() { this.pendingHolds = 0; this.clearedItems = 0; this.flaggedItems = 0; this.disputedItems = 0; }

    post(status, amount) {
        this.entries.push({ status, amount });
        this.balance += amount;
        this.log("posted");
    }

    credit(amount) {
        this.post("posted", amount);
        this.clearedItems += 1;
    }

    debit(amount) {
        this.post("posted", -amount);
        this.clearedItems += 1;
    }

    hold(amount) {
        this.post("pending", amount);
        this.pendingHolds += 1;
    }

    dispute(amount) {
        this.post("disputed", amount);
        this.disputedItems += 1;
        this.flaggedItems += 1;
    }

    transfer(to, amount) {
        this.debit(amount);
        to.credit(amount);
        this.transfers += 1;
    }

    applyInterest(rate) {
        const interest = this.balance * rate;
        this.post("posted", interest);
        this.interestPaid += interest;
    }

    flagLarge(threshold) {
        let n = 0;
        for (const e of this.entries) {
            if (Math.abs(e.amount) > threshold) n += 1;
        }
        this.flaggedItems += n;
        return n;
    }

    largestEntry() {
        let best = 0;
        for (const e of this.entries) {
            if (Math.abs(e.amount) > Math.abs(best)) best = e.amount;
        }
        return best;
    }

    statementLine(i) {
        const e = this.entries[i];
        return e.status + ":" + String(e.amount);
    }

    rename(newName) {
        this.previousName = this.name;
        this.name = newName;
        this.log("renamed");
    }

    netFlow() {
        return this.sumSigned(+1) - this.sumSigned(-1);
    }

    reset() {
        this.entries = [];
        this.summary = new Map();
        this.balance = 0;
        this.log("reset");
    }

    sumSigned(sign) {
        let sum = 0;
        for (const e of this.entries) {
            if ((e.amount >= 0) === (sign > 0)) sum += Math.abs(e.amount);
        }
        return sum;
    }

    countStatus(status) {
        let n = 0;
        for (const e of this.entries) {
            if (e.status === status) n += 1;
        }
        return n;
    }

    setLimit(limit) {
        this.limit = limit;
        this.log("limit changed");
    }

    overLimit() {
        return this.balance < -this.limit;
    }

    entryCount() {
        return this.entries.length;
    }

    summaryValue(key) {
        return this.summary.get(key) ?? 0;
    }
}

module.exports = { Ledger };
