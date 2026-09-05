# churn-demo — what each file pair shows

`old/` and `new/` are two versions of the same small project. CodeDelta compares
them directory-to-directory. Two file families:

## `account.*` (seven languages) — ordinary churn

Small in-place edits, a removed method, an added method. Shows CHG / DEL / ADD /
CRN and REP_CHURN. `package.json` + `package-lock.json` carry the TRUE_CHURN
demonstration: a one-line dependency bump and the lockfile regenerated from it,
classified as generated churn and subtotalled.

## `ledger.*` (seven languages) — moved code is not churn

Each `ledger.*` pair is built so that `git diff --numstat` reports roughly 25
lines deleted and 25 added, while CodeDelta reports one changed statement and
the rest as **moved**:

- **A 20-statement block moved a long way.** `reconcile()` is the first method of
  the class in `old/` and the last in `new/`, jumping over about 50 unchanged
  statements. Its text is byte-identical on both sides.
- **Several statements on one physical line, moved** (C++, Java, JS, TS only).
  `resetCounters()` holds four statements on one line and moves with the
  block. MOV_LLOC counts the four statements; MOV_SLOC counts the one line.
- **One genuine edit** in `post()` (`balance += amount` becomes
  `balance = balance + amount`), so the file also carries real churn: CHG 1.

### Figures (written before the run, then reproduced)

Measured with the CodeDelta engine on these exact files. Git figures from
`git diff --no-index --numstat old/<f> new/<f>`.

| File | git numstat (+/−) | CHG_LLOC | DEL_LLOC | ADD_LLOC | CRN_LLOC | MOV_LLOC | MOV_SLOC |
|---|---|---|---|---|---|---|---|
| ledger.cpp  | +26 / −26 | 1 | 0 | 0 | 1 | 24 | 21 |
| Ledger.java | +26 / −26 | 1 | 0 | 0 | 1 | 24 | 21 |
| ledger.js   | +26 / −26 | 1 | 0 | 0 | 1 | 24 | 24 |
| ledger.ts   | +26 / −26 | 1 | 0 | 0 | 1 | 24 | 24 |
| ledger.go   | +24 / −24 | 1 | 0 | 0 | 1 | 20 | 21 |
| ledger.py   | +23 / −23 | 1 | 0 | 0 | 1 | 21 | 21 |
| ledger.sh   | +24 / −24 | 1 | 0 | 0 | 1 | 21 | 21 |

MOV_SLOC is the number of distinct physical lines the moved statements occupy
(rule of engine 2.0.2 and later). Engine 2.0.1 counted one line per moved
statement, giving 24 for C++/Java and 27 for JS/TS on the dense line; every
other figure in the table is identical on 2.0.1.

Why the per-language MOV counts differ:

- **C++ / Java:** 20 block statements + 4 on the dense line = 24 statements on
  21 lines. Method headers and braces are not statements.
- **JS / TS:** same 24 statements. The JS reader splits on semicolons, so a
  method header rides with the method's first statement; that token spans the
  header line and the previous method's closing brace, hence MOV_SLOC 24.
- **Go:** no dense line (gofmt style). The `func` header rides with the first
  statement, so 20 statements over 21 lines.
- **Python / Shell:** every logical line is a statement, and the `def` /
  function header line is one of them: 21.

### How the fixture is shaped, and why

- **The moved block must be the minority of the file.** A diff is a shortest
  edit script: in a 40-statement file, moving the top 20 to the bottom is the
  same edit as moving the bottom 20 to the top, and git reads it the same way.
  The `ledger.*` body is about 50 statements so the 20-statement block is
  unambiguously the thing that moved.
- **Moved statements must be distinctive.** CodeDelta pairs a deleted and an
  added statement as a move only when the text (whitespace removed) is at
  least 12 characters and occurs exactly once among the file's deletions and
  once among its additions. Repeated trivia (`break;`, `n += 1;`) never counts
  as moved. The dense line uses `pendingHolds = 0;`-style names for that
  reason.
- **The edit must stay an edit.** A deleted/added pair at the same position is
  CHG only if the two texts share at least 30% of their characters as a
  common substring; otherwise DEL + ADD. `balance += amount` to
  `balance = balance + amount` shares 47%.
