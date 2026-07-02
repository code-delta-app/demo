# CodeDelta — demo code

Sample projects used to demonstrate [CodeDelta](https://codedelta.app). They are
fetched on demand by the tool's **Download demo code** option, and can also be
read here on GitHub. Two demos:

- **`churn-demo/`** — an `old/` and `new/` version of the same small project in
  seven languages, to show CodeDelta's churn metrics (CHG / DEL / ADD / CRN /
  REP_CHURN).
- **`agent-scan-demo/`** — a project that *uses* AI at runtime, to show
  CodeDelta's Agent Scan finding AI-SDK calls, agent patterns, and risky usage.

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
