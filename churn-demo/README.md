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
  `balance = balance + amount`), so the file also carries real churn.
- **One edit inside the moved block** (added 6 Sep 2026): the block's last
  statement, `balance = closing`, becomes `balance = closing + interestPaid`.
  Edits trump moves: that statement is counted as CHANGED (churn), not as a
  move, and reported as **changed and moved** (CHM_LLOC). The Code Browser
  paints its two rows red with the navy move edge and the jump chip.

### Figures (written before the run, then reproduced)

Measured with the CodeDelta engine on these exact files. Git figures from
`git diff --no-index --numstat old/<f> new/<f>`.

| File | git numstat (+/−) | CHG_LLOC | DEL_LLOC | ADD_LLOC | CRN_LLOC | MOV_LLOC | CHM_LLOC | MOV_SLOC |
|---|---|---|---|---|---|---|---|---|
| ledger.cpp  | +26 / −26 | 2 | 0 | 0 | 2 | 23 | 1 | 21 |
| Ledger.java | +26 / −26 | 2 | 0 | 0 | 2 | 23 | 1 | 21 |
| ledger.js   | +26 / −26 | 2 | 0 | 0 | 2 | 23 | 1 | 21 |
| ledger.ts   | +26 / −26 | 2 | 0 | 0 | 2 | 23 | 1 | 21 |
| ledger.go   | +24 / −24 | 2 | 0 | 0 | 2 | 19 | 1 | 20 |
| ledger.py   | +23 / −23 | 2 | 0 | 0 | 2 | 20 | 1 | 20 |
| ledger.sh   | +24 / −24 | 2 | 0 | 0 | 2 | 20 | 1 | 20 |

MOV_SLOC is the number of distinct physical lines the moved statements occupy
(engine 2.0.2 and later), plus the block's header line, which moved with it.
CHM_LLOC is the changed-and-moved statement; it is inside CHG_LLOC, not
MOV_LLOC. Engine 2.0.1 has no CHM_LLOC column and differs on MOV_SLOC (it
counted one line per moved statement, and its JS/TS/Go readers carried the
method header inside the first statement). Measured 6 Sep 2026 with the
2.0.2-dev engine at commit 7498d53.

Why the per-language MOV counts differ:

- **C++ / Java:** 20 block statements + 4 on the dense line = 24, of which 23
  moved unchanged and 1 (the last) was edited — changed and moved. Moved
  lines: 19 block lines + the dense line + the `reconcile` header line = 21.
  Braces are not statements; a lone `}` is not credited as a moved line.
- **JS / TS:** same 24 statements, 23 moved + 1 changed and moved, 21 lines.
- **Go:** no dense line (gofmt style): 19 moved + 1 changed and moved; 20
  moved lines including the `func` header.
- **Python / Shell:** every logical line is a statement, and the `def` /
  function header line is one of them: 20 moved + 1 changed and moved.

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
