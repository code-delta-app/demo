#include <string>
#include <vector>

class Account {
public:
    Account(const std::string& owner, double balance)
        : owner_(owner), balance_(balance) {}

    void deposit(double amount) {
        balance_ += amount;
        history_.push_back("deposit");
    }

    void withdraw(double amount) {
        balance_ -= amount;
        history_.push_back("withdraw");
    }

    void applyFee(double fee) {
        balance_ -= fee;
        history_.push_back("fee");
    }

    double getBalance() const {
        return balance_;
    }

    std::string getOwner() const {
        return owner_;
    }

    bool isOverdrawn() const {
        return balance_ < 0;
    }

    int historyCount() const {
        return history_.size();
    }

    void printStatement() const {
        for (const auto& e : history_) {
            log(e);
        }
    }

private:
    void log(const std::string& m) const {}
    std::string owner_;
    double balance_;
    std::vector<std::string> history_;
};
