# Meridian Helpdesk — Churn + Agent Scan, every safety surface in one run

Two versions of the same product (`old/`, `new/`). Between them a release added the AI features —
and with them the 32 CRITICAL files described in `agent-scan-demo/README.md` — while the
**build machinery changed underneath**: 20 build, CI, packaging and dependency files changed in one
diff. Every build file is written for Meridian (the Python core, the Go CLI, the web widget, the
native gateway) and every one is inert: `example.invalid` does not resolve, nothing is executed.

Run it the way the GitHub Action runs a pull request: **Try It — Demos → Churn + Agent Scan
Demo → Run**, or:

```bash
codedelta-gui scan <folder>/new <folder>/old --mode churn_agent
```

## What the build side shows — "Build Files Changed In This Diff (20)"

The report sorts the changed build files into tiers, most urgent first:

**Install / build hooks (code runs on install) — 2**
- `setup.py` — added
- `package.json` — modified
  `setup.py`'s post-install hook fetches and runs a remote script; `package.json`'s postinstall
  runs `build/postinstall.js` — the s1ngularity card from the Agent Scan demo, wired into the
  manifest so the two findings are one story.

**Fetches remote content at build time — 4**
- `CMakeLists.txt` — deleted
- `Makefile` — modified, fetches `https://toolchain.example.invalid/install.sh`
- `native/gateway/Makefile` — added
- `Dockerfile` — modified, fetches `https://toolchain.example.invalid/agent.sh`
  The root Makefile grew a `toolchain` target that pipes a download into `sh` and made `build`
  depend on it; the native gateway's CMake build was deleted and replaced by a Makefile that
  fetches a "prebuilt" dependency; the Dockerfile fetches an agent installer and hands its
  entrypoint to `codex exec --full-auto`.

**CI / CD pipelines** — `Jenkinsfile` deleted (it ran `codex exec --full-auto` on failure);
`.gitlab-ci.yml` modified to run `codex` with approvals and sandbox bypassed (rated **CRITICAL**
in the same run); `.github/workflows/autofix.yml` (**CRITICAL**), `ci.yml` and `release.yml` added.

**Build definitions** — `configure.ac` and `m4/ax_check_net.m4` added. The macro mirrors the
xz-utils shape: an innocuous header probe that, when a particular fixture file is present in the
source tree, rewrites a build step at configure time. (The fixture is not present; the macro is a
shape, not a working injection.)

**Packaging / containers** — `debian/control`, `debian/rules`, `docker-compose.yml` added.

**Dependency manifests** — `Cargo.lock` deleted, `go.sum` added, `requirements.txt` modified
(the AI SDKs arrive: openai, anthropic, langchain, crewai, ollama), `web/package-lock.json` bumped.

The Dockerfile also appears as a **HIGH** card (an agent CLI launched as the container's
entrypoint). Makefiles and CMake files carry no agent rules, so their fetches surface in the build
section only — that is by design: the build section is the place to review them.

## What the churn side shows

Every churn tile is non-zero by construction:

| Tile | Where it comes from |
|------|--------------------|
| CHG / DEL / ADD | edits in `helpdesk/tickets.py`, `helpdesk/priority.py` (a loop rewritten in place), `helpdesk/legacy_csv.py` removed, `helpdesk/util_dates.py` added — plus the new files |
| MOV and CHM | `helpdesk/sla.py`: a function moved within the file verbatim, with one line edited inside the moved block (MOV 2, CHM 1) |
| Comment churn | `helpdesk/store.py` and `helpdesk/sla.py`: comments changed, deleted and added (CHG 5, DEL 1, ADD 5) |
| REWRITE | `helpdesk/priority.py`: statements torn out and rewritten where they stood (3) |
| Generated churn / TRUE_CHURN | `web/package-lock.json`: a version bump in a lockfile — counted in CHURN, subtotalled out of TRUE_CHURN |
| DATA tiles | `native/tables/status_codes.c` (a table deleted, one added, one shrunk) and `native/tables/mime_types.c` (one grown) |
| Build Files Changed | the 20 files above, hooks first |

Expected (LLOC): **CHG 20, DEL 26, ADD 314, CHURN 360, TRUE_CHURN 354**
(6 generated); files 12 changed, 49 new, 4 deleted, 42 unchanged. The changed-file rows the demo
page checks against its frozen values:

| File | CHG | DEL | ADD | CRN | REP_CHURN |
|---|---|---|---|---|---|
| `.gitlab-ci.yml` | 1 | 0 | 7 | 8 | 0.88 |
| `Dockerfile` | 1 | 1 | 1 | 3 | 0.67 |
| `Makefile` | 2 | 0 | 2 | 4 | 0.50 |
| `helpdesk/priority.py` | 1 | 4 | 4 | 9 | 0.89 |
| `helpdesk/sla.py` | 1 | 0 | 0 | 1 | 0.00 |
| `helpdesk/store.py` | 0 | 0 | 0 | 0 |  |
| `helpdesk/tickets.py` | 1 | 0 | 7 | 8 | 0.88 |
| `native/tables/mime_types.c` | 1 | 0 | 0 | 1 | 0.00 |
| `native/tables/status_codes.c` | 2 | 1 | 1 | 4 | 0.50 |
| `package.json` | 4 | 0 | 3 | 7 | 0.43 |
| `requirements.txt` | 0 | 0 | 6 | 6 | 1.00 |
| `web/package-lock.json` | 6 | 0 | 0 | 6 | 0.00 |

The agent side of the same run: **32 CRITICAL, 3 HIGH, 28 ELEVATED** — the
Agent Scan demo's cards plus the CI recipe and the Dockerfile, all of them new in this version.

Every figure was produced by the tool on these folders.
