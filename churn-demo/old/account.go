package bank

type Account struct {
	owner   string
	balance float64
	history []string
}

func NewAccount(owner string, balance float64) *Account {
	return &Account{owner: owner, balance: balance, history: []string{}}
}

func (a *Account) Deposit(amount float64) {
	a.balance += amount
	a.history = append(a.history, "deposit")
}

func (a *Account) Withdraw(amount float64) {
	a.balance -= amount
	a.history = append(a.history, "withdraw")
}

func (a *Account) ApplyFee(fee float64) {
	a.balance -= fee
	a.history = append(a.history, "fee")
}

func (a *Account) Balance() float64 {
	return a.balance
}

func (a *Account) IsOverdrawn() bool {
	return a.balance < 0
}

func (a *Account) HistoryCount() int {
	return len(a.history)
}

func (a *Account) PrintStatement() {
	for _, e := range a.history {
		println(e)
	}
}
