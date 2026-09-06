import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Ledger {
    private String name;
    private String previousName;
    private double balance;
    private double limit;
    private double interestPaid = 0.0;
    private int transfers = 0;
    private int pendingHolds = 0;
    private int clearedItems = 0;
    private int flaggedItems = 0;
    private int disputedItems = 0;
    private final List<Entry> entries = new ArrayList<>();
    private final Map<String, Double> summary = new HashMap<>();

    static final class Entry {
        final String status;
        final double amount;
        Entry(String status, double amount) { this.status = status; this.amount = amount; }
    }

    public Ledger(String name) {
        this.name = name;
        this.balance = 0.0;
        this.limit = 0.0;
    }

    public void post(String status, double amount) {
        entries.add(new Entry(status, amount));
        balance = balance + amount;
        log("posted");
    }

    public void credit(double amount) {
        post("posted", amount);
        clearedItems += 1;
    }

    public void debit(double amount) {
        post("posted", -amount);
        clearedItems += 1;
    }

    public void hold(double amount) {
        post("pending", amount);
        pendingHolds += 1;
    }

    public void dispute(double amount) {
        post("disputed", amount);
        disputedItems += 1;
        flaggedItems += 1;
    }

    public void transfer(Ledger to, double amount) {
        debit(amount);
        to.credit(amount);
        transfers += 1;
    }

    public void applyInterest(double rate) {
        double interest = balance * rate;
        post("posted", interest);
        interestPaid += interest;
    }

    public int flagLarge(double threshold) {
        int n = 0;
        for (Entry e : entries) {
            if (Math.abs(e.amount) > threshold) n += 1;
        }
        flaggedItems += n;
        return n;
    }

    public double largestEntry() {
        double best = 0.0;
        for (Entry e : entries) {
            if (Math.abs(e.amount) > Math.abs(best)) best = e.amount;
        }
        return best;
    }

    public String statementLine(int i) {
        Entry e = entries.get(i);
        return e.status + ":" + e.amount;
    }

    public void rename(String newName) {
        previousName = name;
        name = newName;
        log("renamed");
    }

    public double netFlow() {
        return sumSigned(+1) - sumSigned(-1);
    }

    public void reset() {
        entries.clear();
        summary.clear();
        balance = 0.0;
        log("reset");
    }

    public double sumSigned(int sign) {
        double sum = 0.0;
        for (Entry e : entries) {
            if ((e.amount >= 0) == (sign > 0)) sum += Math.abs(e.amount);
        }
        return sum;
    }

    public int countStatus(String status) {
        int n = 0;
        for (Entry e : entries) {
            if (e.status.equals(status)) n += 1;
        }
        return n;
    }

    public void setLimit(double limit) {
        this.limit = limit;
        log("limit changed");
    }

    public boolean overLimit() {
        return balance < -limit;
    }

    public String getName() {
        return name;
    }

    public double getBalance() {
        return balance;
    }

    public int entryCount() {
        return entries.size();
    }

    public double summaryValue(String key) {
        return summary.getOrDefault(key, 0.0);
    }

    public void reconcile() {
        double opening = balance;
        double credits = sumSigned(+1);
        double debits = sumSigned(-1);
        double closing = opening + credits - debits;
        double drift = closing - balance;
        int postedCount = countStatus("posted");
        int pendingCount = countStatus("pending");
        int disputedCount = countStatus("disputed");
        int total = postedCount + pendingCount + disputedCount;
        double average = total > 0 ? (credits + debits) / total : 0.0;
        summary.put("opening", opening);
        summary.put("credits", credits);
        summary.put("debits", debits);
        summary.put("closing", closing);
        summary.put("drift", drift);
        summary.put("posted", (double) postedCount);
        summary.put("pending", (double) pendingCount);
        summary.put("disputed", (double) disputedCount);
        summary.put("average", average);
        balance = closing + interestPaid;
    }

    public void resetCounters() { pendingHolds = 0; clearedItems = 0; flaggedItems = 0; disputedItems = 0; }

    private void log(String m) {}
}
