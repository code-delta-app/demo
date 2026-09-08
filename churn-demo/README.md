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
- **One edit inside the moved block**: the block's last
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
MOV_LLOC. (CodeDelta 2.0.1 had no CHM_LLOC column and counted MOV_SLOC as one
line per moved statement; the figures here are from CodeDelta 2.0.2.)

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

## Comment churn, an added file and a deleted file

So that every tile on the app's panel has a value to show:

- `ledger.cpp` and `ledger.py` each carry three comment lines in the old version:
  one is **edited** in the new version, one is **removed**, and one new comment is
  **added** at the end of the file. Measured: CHG_COM 1 / DEL_COM 1 / ADD_COM 1 per
  file, 2 / 2 / 2 in total. Comment churn never touches the LLOC or SLOC figures —
  the ledger rows above are unchanged.
- `audit.py` exists only in the new version (ADD_FILE 1, ADD_LLOC 8).
- `legacy_export.sh` exists only in the old version (DEL_FILE 1, DEL_LLOC 5).

Totals for the pair on CodeDelta 2.0.2: 18 files, 16 changed, 1 added,
1 deleted; CHG_LLOC 464, DEL_LLOC 207, ADD_LLOC 287, MOV_LLOC 162, CHM_LLOC 7,
CRN_LLOC 958; CHG_COM 2, DEL_COM 2, ADD_COM 2.
