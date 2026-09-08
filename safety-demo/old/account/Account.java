import java.util.ArrayList;
import java.util.List;

public class Account {
    private String owner;
    private double balance;
    private List<String> history = new ArrayList<>();

    public Account(String owner, double balance) {
        this.owner = owner;
        this.balance = balance;
    }

    public void deposit(double amount) {
        balance += amount;
        history.add("deposit");
    }

    public void withdraw(double amount) {
        balance -= amount;
        history.add("withdraw");
    }

    public void applyFee(double fee) {
        balance -= fee;
        history.add("fee");
    }

    public double getBalance() {
        return balance;
    }

    public boolean isOverdrawn() {
        return balance < 0;
    }

    public int historyCount() {
        return history.size();
    }

    public void printStatement() {
        for (String e : history) {
            System.out.println(e);
        }
    }
}
