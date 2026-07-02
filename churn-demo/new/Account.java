import java.util.ArrayList;
import java.util.List;

public class Account {
    private String owner;
    private double balance;
    private double minBalance = 0.0;
    private List<String> history = new ArrayList<>();

    public Account(String owner, double balance) {
        this.owner = owner;
        this.balance = balance;
    }

    public void deposit(double amount) {
        balance = balance + amount;
        history.add("DEPOSIT");
    }

    public void withdraw(double amount) {
        balance = balance - amount;
        history.add("WITHDRAW");
    }

    public void applyFee(double fee) {
        balance = balance - fee;
        history.add("FEE");
    }

    public double getBalance() {
        return balance;
    }

    public boolean isOverdrawn() {
        return balance < minBalance;
    }

    public int historyCount() {
        return history.size();
    }

    public void applyInterest(double rate) {
        balance = balance + balance * rate;
        history.add("INTEREST");
    }

    public boolean transfer(Account to, double amount) {
        balance = balance - amount;
        to.balance = to.balance + amount;
        return true;
    }
}
