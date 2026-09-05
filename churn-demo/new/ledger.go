package ledger

import (
	"fmt"
	"math"
)

type Entry struct {
	Status string
	Amount float64
}

type Ledger struct {
	name          string
	previousName  string
	balance       float64
	limit         float64
	interestPaid  float64
	transfers     int
	pendingHolds  int
	clearedItems  int
	flaggedItems  int
	disputedItems int
	entries       []Entry
	summary       map[string]float64
}

func NewLedger(name string) *Ledger {
	return &Ledger{name: name, summary: map[string]float64{}}
}

func averageOf(sum float64, n int) float64 {
	if n == 0 {
		return 0
	}
	return sum / float64(n)
}

func (l *Ledger) Post(status string, amount float64) {
	l.entries = append(l.entries, Entry{Status: status, Amount: amount})
	l.balance = l.balance + amount
	l.log("posted")
}

func (l *Ledger) Credit(amount float64) {
	l.Post("posted", amount)
	l.clearedItems++
}

func (l *Ledger) Debit(amount float64) {
	l.Post("posted", -amount)
	l.clearedItems++
}

func (l *Ledger) Hold(amount float64) {
	l.Post("pending", amount)
	l.pendingHolds++
}

func (l *Ledger) Dispute(amount float64) {
	l.Post("disputed", amount)
	l.disputedItems++
	l.flaggedItems++
}

func (l *Ledger) Transfer(to *Ledger, amount float64) {
	l.Debit(amount)
	to.Credit(amount)
	l.transfers++
}

func (l *Ledger) ApplyInterest(rate float64) {
	interest := l.balance * rate
	l.Post("posted", interest)
	l.interestPaid += interest
}

func (l *Ledger) FlagLarge(threshold float64) int {
	n := 0
	for _, e := range l.entries {
		if math.Abs(e.Amount) > threshold {
			n++
		}
	}
	l.flaggedItems += n
	return n
}

func (l *Ledger) LargestEntry() float64 {
	best := 0.0
	for _, e := range l.entries {
		if math.Abs(e.Amount) > math.Abs(best) {
			best = e.Amount
		}
	}
	return best
}

func (l *Ledger) StatementLine(i int) string {
	e := l.entries[i]
	return fmt.Sprintf("%s:%.2f", e.Status, e.Amount)
}

func (l *Ledger) Rename(newName string) {
	l.previousName = l.name
	l.name = newName
	l.log("renamed")
}

func (l *Ledger) NetFlow() float64 {
	return l.sumSigned(+1) - l.sumSigned(-1)
}

func (l *Ledger) Reset() {
	l.entries = nil
	l.summary = map[string]float64{}
	l.balance = 0
	l.log("reset")
}

func (l *Ledger) sumSigned(sign int) float64 {
	sum := 0.0
	for _, e := range l.entries {
		if (e.Amount >= 0) == (sign > 0) {
			sum += math.Abs(e.Amount)
		}
	}
	return sum
}

func (l *Ledger) countStatus(status string) int {
	n := 0
	for _, e := range l.entries {
		if e.Status == status {
			n++
		}
	}
	return n
}

func (l *Ledger) SetLimit(limit float64) {
	l.limit = limit
	l.log("limit changed")
}

func (l *Ledger) OverLimit() bool {
	return l.balance < -l.limit
}

func (l *Ledger) Name() string {
	return l.name
}

func (l *Ledger) Balance() float64 {
	return l.balance
}

func (l *Ledger) EntryCount() int {
	return len(l.entries)
}

func (l *Ledger) SummaryValue(key string) float64 {
	return l.summary[key]
}

func (l *Ledger) Reconcile() {
	opening := l.balance
	credits := l.sumSigned(+1)
	debits := l.sumSigned(-1)
	closing := opening + credits - debits
	drift := closing - l.balance
	posted := l.countStatus("posted")
	pending := l.countStatus("pending")
	disputed := l.countStatus("disputed")
	total := posted + pending + disputed
	average := averageOf(credits+debits, total)
	l.summary["opening"] = opening
	l.summary["credits"] = credits
	l.summary["debits"] = debits
	l.summary["closing"] = closing
	l.summary["drift"] = drift
	l.summary["posted"] = float64(posted)
	l.summary["pending"] = float64(pending)
	l.summary["disputed"] = float64(disputed)
	l.summary["average"] = average
	l.balance = closing
}

func (l *Ledger) log(m string) {}
