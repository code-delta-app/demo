package bank

type Account struct {
	owner      string
	balance    float64
	minBalance float64
	history    []string
}

func NewAccount(owner string, balance float64) *Account {
	return &Account{owner: owner, balance: balance, minBalance: 0.0, history: []string{}}
}

func (a *Account) Deposit(amount float64) {
	a.balance = a.balance + amount
	a.history = append(a.history, "DEPOSIT")
}

func (a *Account) Withdraw(amount float64) {
	a.balance = a.balance - amount
	a.history = append(a.history, "WITHDRAW")
}

func (a *Account) ApplyFee(fee float64) {
	a.balance = a.balance - fee
	a.history = append(a.history, "FEE")
}

func (a *Account) Balance() float64 {
	return a.balance
}

func (a *Account) IsOverdrawn() bool {
	return a.balance < a.minBalance
}

func (a *Account) HistoryCount() int {
	return len(a.history)
}

func (a *Account) ApplyInterest(rate float64) {
	a.balance = a.balance +
		a.balance*rate
	a.history = append(a.history, "INTEREST")
}
