# safety-demo — Churn + Agent Scan, every safety surface in one run

Two versions of a small C + Python service (`old/`, `new/`). Between them the
**build machinery changes** and the synthetic AI-agent files from
`agent-scan-demo` sit under `agent/` in both versions.

Run it the way the GitHub Action runs a pull request — Churn + Agent Scan:

    python3 codedelta_server.py scan safety-demo/new safety-demo/old --mode churn_agent --html

## What changes between old and new

| Kind | Files |
|---|---|
| Install / build hooks | `setup.py` added with an install hook; `package.json` gains a hook |
| Build definitions | `Makefile` modified; `CMakeLists.txt` deleted; `configure.ac`, `m4/ax_check_net.m4` added |
| CI / CD pipelines | `.github/workflows/ci.yml`, `.github/workflows/release.yml` added; `.gitlab-ci.yml` modified; `Jenkinsfile` deleted |
| Packaging / containers | `Dockerfile` modified; `buildproj.spec` deleted; `debian/control`, `debian/rules`, `docker-compose.yml` added |
| Dependency manifests | `Cargo.lock` deleted; `go.sum` added; `requirements.txt` modified |
| Source | `src/net.c`, `src/net.h` added; edits in `src/*.c`, `app/*.py`, `tools/gen_report.py` |

## What the agent report shows (measured on CodeDelta 2.0.1, 7 Sep 2026)

- **Build Files Changed In This Diff (18)**: 15 build/CI/packaging files plus 3 dependency manifests, with the two install hooks flagged
- **Build & Deployment Surface (12)**: the inventory of the new version's build files
- **Committed Credentials (1)** and **Agent Infrastructure (6, 2 tier-3)** from `agent/openclaw/`, `agent/.claude/`, `agent/.mcp.json`
- **Governance & Compliance**: data egress to CN and RU providers
- **AI SDK Inventory**, **Flagged Files** (22 scanned: 3 HIGH, 8 ELEVATED), **Agent Map**
- The Code Browser opens with an **Agents** view of the same map

Churn (new vs old): 55 files, 13 changed, 11 added, 4 deleted;
CHG_LLOC 18, DEL_LLOC 14, ADD_LLOC 128, CRN_LLOC 160.

Everything under `agent/` is inert: fake, non-working "agents" with no real keys,
no network calls, never executed — CodeDelta only reads them as text. Antivirus
tooling may flag them; that is expected.
