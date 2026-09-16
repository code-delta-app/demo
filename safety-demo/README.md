# Meridian Helpdesk — Churn + Agent Scan, every safety surface in one run

Two versions of the same product (`old/`, `new/`). Between them a release added the AI
features — and with them the fifteen risky files described in `agent-scan-demo/README.md`
— while the **build machinery** changed underneath: an install hook arrived in `setup.py`,
`package.json` gained a hook, the `Makefile` and `Dockerfile` were modified, `CMakeLists.txt`,
the `Jenkinsfile` and `Cargo.lock` were deleted, two GitHub workflows, `configure.ac`, an
Autoconf macro, Debian packaging and `docker-compose.yml` were added. Twenty build files
changed in one diff — the xz-utils entry route, in miniature.

Run it the way the GitHub Action runs a pull request: **Try It — Demos → Churn + Agent
Scan Demo → Run**, or:

```bash
codedelta-gui scan <folder>/new <folder>/old --mode churn_agent
```

## What the churn side shows

Every churn tile is non-zero by construction:

| Tile | Where it comes from |
|------|--------------------|
| CHG / DEL / ADD | edits in `helpdesk/tickets.py` (a method added, one edited), `helpdesk/priority.py` (a loop rewritten in place), `helpdesk/legacy_csv.py` removed, `helpdesk/util_dates.py` added — plus the thirty-one new files |
| MOV and CHM | `helpdesk/sla.py`: a function moved within the file verbatim, with one line edited inside the moved block ("changed and moved") |
| Comment churn | `helpdesk/store.py`: a comment changed and two deleted; `helpdesk/sla.py`: one added |
| REWRITE | `helpdesk/priority.py`: two statements torn out and rewritten where they stood |
| Generated churn / TRUE_CHURN | `web/package-lock.json`: a version bump in a lockfile — counted in CHURN, subtotalled out of TRUE_CHURN |
| DATA tiles | `native/tables/status_codes.c` (a table deleted, one added, one shrunk) and `native/tables/mime_types.c` (one grown) |
| Build & Deployment Surface | the twenty build files above, the install hook first |

Expected (LLOC): **CHG 27, DEL 31, ADD 229, CHURN 287, TRUE_CHURN 281**; files 12 changed,
31 new, 5 deleted, 27 unchanged. The agent side of the same run: the fifteen CRITICAL
cards of the Agent Scan demo, all of them new in this version.

Every figure was produced by the tool on these folders.
