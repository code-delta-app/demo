#include <cmath>
#include <string>
#include <vector>
#include <map>

struct Entry {
    std::string status;
    double amount;
};

class Ledger {
public:
    Ledger(const std::string& name) : name_(name), balance_(0.0), limit_(0.0) {}

    void post(const std::string& status, double amount) {
        entries_.push_back(Entry{status, amount});
        balance_ = balance_ + amount;
        log("posted");
    }

    void credit(double amount) {
        post("posted", amount);
        clearedItems_ += 1;
    }

    void debit(double amount) {
        post("posted", -amount);
        clearedItems_ += 1;
    }

    void hold(double amount) {
        post("pending", amount);
        pendingHolds_ += 1;
    }

    void dispute(double amount) {
        post("disputed", amount);
        disputedItems_ += 1;
        flaggedItems_ += 1;
    }

    void transfer(Ledger& to, double amount) {
        debit(amount);
        to.credit(amount);
        transfers_ += 1;
    }

    void applyInterest(double rate) {
        double interest = balance_ * rate;
        post("posted", interest);
        interestPaid_ += interest;
    }

    int flagLarge(double threshold) {
        int n = 0;
        for (const auto& e : entries_) {
            if (std::abs(e.amount) > threshold) n += 1;
        }
        flaggedItems_ += n;
        return n;
    }

    double largestEntry() const {
        double best = 0.0;
        for (const auto& e : entries_) {
            if (std::abs(e.amount) > std::abs(best)) best = e.amount;
        }
        return best;
    }

    std::string statementLine(int i) const {
        const Entry& e = entries_.at(i);
        return e.status + ":" + std::to_string(e.amount);
    }

    void rename(const std::string& newName) {
        previousName_ = name_;
        name_ = newName;
        log("renamed");
    }

    double netFlow() const {
        return sumSigned(+1) - sumSigned(-1);
    }

    void reset() {
        entries_.clear();
        summary_.clear();
        balance_ = 0.0;
        log("reset");
    }

    double sumSigned(int sign) const {
        double sum = 0.0;
        for (const auto& e : entries_) {
            if ((e.amount >= 0) == (sign > 0)) sum += std::abs(e.amount);
        }
        return sum;
    }

    int countStatus(const std::string& status) const {
        int n = 0;
        for (const auto& e : entries_) {
            if (e.status == status) n += 1;
        }
        return n;
    }

    void setLimit(double limit) {
        limit_ = limit;
        log("limit changed");
    }

    bool overLimit() const {
        return balance_ < -limit_;
    }

    std::string name() const {
        return name_;
    }

    double balance() const {
        return balance_;
    }

    int entryCount() const {
        return static_cast<int>(entries_.size());
    }

    double summaryValue(const std::string& key) const {
        auto it = summary_.find(key);
        return it == summary_.end() ? 0.0 : it->second;
    }

    void reconcile() {
        double opening = balance_;
        double credits = sumSigned(+1);
        double debits = sumSigned(-1);
        double closing = opening + credits - debits;
        double drift = closing - balance_;
        int posted = countStatus("posted");
        int pending = countStatus("pending");
        int disputed = countStatus("disputed");
        int total = posted + pending + disputed;
        double average = total > 0 ? (credits + debits) / total : 0.0;
        summary_["opening"] = opening;
        summary_["credits"] = credits;
        summary_["debits"] = debits;
        summary_["closing"] = closing;
        summary_["drift"] = drift;
        summary_["posted"] = posted;
        summary_["pending"] = pending;
        summary_["disputed"] = disputed;
        summary_["average"] = average;
        balance_ = closing;
    }

    void resetCounters() { pendingHolds_ = 0; clearedItems_ = 0; flaggedItems_ = 0; disputedItems_ = 0; }

private:
    void log(const std::string& m) const {}
    std::string name_;
    std::string previousName_;
    double balance_;
    double limit_;
    double interestPaid_ = 0.0;
    int transfers_ = 0;
    int pendingHolds_ = 0;
    int clearedItems_ = 0;
    int flaggedItems_ = 0;
    int disputedItems_ = 0;
    std::vector<Entry> entries_;
    std::map<std::string, double> summary_;
};
