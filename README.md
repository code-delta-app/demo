# CodeDelta — demo code

Sample projects used to demonstrate [CodeDelta](https://codedelta.app). They are
fetched on demand by the tool's **Download demo code** option, and can also be
read here on GitHub. Three demos:

- **`churn-demo/`** — an `old/` and `new/` version of the same small project in
  seven languages, to show CodeDelta's churn metrics (CHG / DEL / ADD / CRN /
  REP_CHURN). Also carries the canonical **TRUE_CHURN** demonstration
  a one-line `package.json` dependency bump alongside the
  `package-lock.json` the tooling regenerated from it — the lockfile churn is
  classified as generated ("npm lockfile") and subtotalled, so the report's
  TRUE_CHURN row/tile shows the churn the developers actually authored.
  The `ledger.*` pairs show **moved code**: a 20-statement block
  moved to the far end of the file, and one line holding four statements
  moved with it — git counts ~25 lines deleted and ~25 added, CodeDelta
  counts them as MOV and reports the single real edit as CHG 1. Expected
  figures and the fixture rules are in `churn-demo/README.md`.
- **`agent-scan-demo/`** — a project that *uses* AI at runtime, to show
  CodeDelta's Agent Scan finding AI-SDK calls, agent patterns, risky usage and
  AI code hidden in encoded strings. Java, C# and C++ agent classes let the Code
  Browser's Classes tab and class visualiser populate too.
- **`safety-demo/`** — two versions of a small C + Python service whose build
  machinery changes (install hooks, a deleted Jenkinsfile, new workflows, Debian
  packaging) beside the synthetic agent files: the Churn + Agent Scan demo, every
  safety surface in one run. Figures in `safety-demo/README.md`.

## ⚠️ Please read first — these files are deliberately suspicious-*looking*

Some files here are **named for the risk they illustrate**, not because they do
anything harmful. They exist so CodeDelta has something to flag in a demo.

**They are inert.** Specifically:

- **Nothing is ever executed.** CodeDelta only ever *reads* these files as text
  (churn diff) or *statically parses* them (Agent Scan). The demo never runs them,
  and neither does anything else — they are scan targets, not programs to launch.
- **No real credentials, no real calls.** API keys are placeholders (`"..."`); no
  network request is ever made. `raw_http.py` and `model_gateway.go` contain the
  *shape* of a call to an AI endpoint so the scanner can detect it — they are not
  invoked.
- **The "committed credentials" are fakes by construction.** CodeDelta's
  committed-credential detection needs something to find, so `openclaw/`
  carries `backup.env` with **Amazon's own published documentation example
  key** (`AKIAIOSFODNN7EXAMPLE` — printed in AWS's docs precisely so it can
  appear in examples) and `deploy_key.pem`, a private-key *header* with no key
  material. Neither opens anything, anywhere.
- **The names describe functionality.** `chinese_models.py` illustrates detection
  of non-Western model SDKs (DeepSeek, Qwen, Zhipu) — it imports their SDK *names*
  so the scanner matches them; it calls nothing. `rogue_executor.py` shows the
  `exec`/`eval`-on-model-output pattern CodeDelta rates HIGH/CRITICAL — it is the
  thing you want a tool to *catch*, presented here as a fixed example.

In short: this is the corpus a static analyzer is *supposed* to find problems in.
A security review of these files is welcome — that's why they're public and
documented. Per-file expectations are in each demo's own README.

## Versioning

The CodeDelta tool fetches a **tagged release** of this repo matching its own
version, so the demo a given build shows never changes underneath it. `main` may
move ahead of released tools.
