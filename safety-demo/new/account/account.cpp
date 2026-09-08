#include <string>
#include <vector>

class Account {
public:
    Account(const std::string& owner, double balance)
        : owner_(owner), balance_(balance) {}

    void deposit(double amount) {
        balance_ = balance_ + amount;
        history_.push_back("DEPOSIT");
    }

    void withdraw(double amount) {
        balance_ = balance_ - amount;
        history_.push_back("WITHDRAW");
    }

    void applyFee(double fee) {
        balance_ = balance_ - fee;
        history_.push_back("FEE");
    }

    double getBalance() const {
        return balance_;
    }

    std::string getOwner() const {
        return owner_;
    }

    bool isOverdrawn() const {
        return balance_ < minBalance_;
    }

    int historyCount() const {
        return (int) history_.size();
    }

    void applyInterest(double rate) {
        balance_ = balance_ + balance_ * rate;
        history_.push_back("INTEREST");
    }

    bool transfer(Account& to, double amount) {
        balance_ = balance_ - amount;
        to.balance_ = to.balance_ + amount;
        return true;
    }

private:
    std::string owner_;
    double balance_;
    double minBalance_ = 0.0;
    std::vector<std::string> history_;
};
