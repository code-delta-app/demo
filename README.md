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
- **`agent-scan-demo/`** — *Meridian Helpdesk*, a fictional support product in twenty-six
  languages and file types whose release added AI features in the exact shapes of the 2025 incidents
  (a supply-chain post-install launching agents with their checks off, an encoded prompt
  sent to a hosted model, a local model with no address in the file, an executing
  notebook, a CI recipe launching an agent, browser and mobile clients that run what a
  model returns). Thirty-one CRITICAL cards across twenty-six languages and file types; the README is a guided tour.
- **`safety-demo/`** — the same product as an `old/` and `new/` pair: the release that
  added the AI features, with the build machinery changing underneath it (two install
  hooks, four build files that fetch remote content, deleted and added CI files, Autoconf, Debian
  packaging — twenty build files in one diff). The Churn + Agent Scan demo:
  every churn tile lit — moves, in-place edits, comment churn, a rewrite, generated
  churn, data tables — beside the agent findings and the Build & Deployment Surface.