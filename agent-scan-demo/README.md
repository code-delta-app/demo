# Meridian Helpdesk — the Agent Scan demo

A fictional customer-support product: a Python core, a Go CLI, a web widget, Java and C#
services, a C++ gateway, mobile clients, an ops toolkit and a CI pipeline. Fifty-eight
files. Every one of them is inert — nothing here contacts a model or runs anything — but
fifteen of them are written in the exact shape of the ways AI has been abused inside real
software in 2025. Agent Scan finds each one and says which.

Run it from the app: **Try It — Demos → Agent Scan Demo → Run**, or from the command line
on the folder the app downloaded:

```bash
codedelta-gui scan <folder> --mode agent
```

Expected: **15 CRITICAL, 2 HIGH, 13 ELEVATED, 28 NORMAL.** The summary line leads with
the threats in words; "Start here" under it links the three highest-scoring cards.

## The tour — one card per threat

| Card | What it mirrors | Where it sits | Rated |
|------|-----------------|---------------|-------|
| `build/postinstall.js` | The nx "s1ngularity" supply-chain attack (Aug 2025): a post-install script that launches the developer's own Claude and Gemini command-line agents with their safety checks switched off | the build folder | **CRITICAL** |
| `helpdesk/telemetry/update_check.py` | LameHug (Jul 2025): the instructions to the model hidden as a base64 string, sent to a hosted model, the reply run as a command | a telemetry helper | **CRITICAL** |
| `helpdesk/local_assistant.py` | PromptLock (Aug 2025): a model running on the local machine — reached through the Ollama library, no address anywhere in the file — whose reply is executed | the helpdesk core | **CRITICAL** |
| `scripts/bootstrap.sh` | the same shape in shell: `OLLAMA_HOST`, `ollama run`, `eval` of the reply | an ops script | **CRITICAL** |
| `.github/workflows/autofix.yml` | a CI recipe running `codex exec` with approvals bypassed on every push | the pipeline | **CRITICAL** |
| `notebooks/explore.ipynb` | a notebook whose third cell `exec`s what the model returned — the finding names the line **and the cell** | the data folder | **CRITICAL** |
| `web/widget.html`, `web/src/components/AssistantPanel.vue` | a page and a Vue component that `fetch` a model and `eval` the reply in the browser | the web front end | **CRITICAL** |
| `mobile/android/…/Assistant.kt`, `mobile/ios/…/Chat.swift`, `mobile/flutter/lib/auto_reply.dart` | three mobile apps (Kotlin, Swift, Dart) that hand the model's reply to a process launcher | the mobile clients | **CRITICAL** |
| `ops/windows/Invoke-AutoFix.ps1` | PowerShell: `Invoke-Expression` on the model's answer | the ops toolkit | **CRITICAL** |
| `helpdesk/telemetry/beacon.py` | an AI-calling program hidden as an encoded string and executed | a telemetry helper | **CRITICAL** |
| `helpdesk/autofix.py` | the classic: `exec` on model output | the helpdesk core | **CRITICAL** |
| `native/gateway/ModelGateway.cpp` | C++: a raw HTTP call to a model, `system()` on the reply | the native gateway | **CRITICAL** |
| `helpdesk/crew.py` | LangChain + CrewAI: autonomous crews spun up from code | the helpdesk core | **HIGH** |
| `helpdesk/digest.py` | a model called inside a loop, and the model is hosted in China | the helpdesk core | **HIGH** |
| `helpdesk/providers/cn.py`, `helpdesk/providers/ru.py` | data leaving for models hosted in CN and RU — the sovereignty finding | provider adapters | **ELEVATED** |
| `helpdesk/telemetry/beacon_disabled.py` | the same encoded payload as `beacon.py`, present but never executed | a telemetry helper | **ELEVATED** |
| `docs/RUNBOOK.md` | a Markdown runbook whose fenced code block is in the rogue shape — documentation is not executed, so it is capped at ELEVATED | the docs | **ELEVATED** |
| `helpdesk/triage.py`, `helpdesk/prompts.py`, `helpdesk/raw_client.py`, `web/app.js`, `cli/internal/gateway/router.go`, `services/…/SupportAgent.java`, `services/planner/AzureChat.cs`, `native/gateway/ModelGateway.hpp`, `mobile/flutter/lib/assistant.dart` | ordinary AI use: an SDK import, a model call, the reply printed | throughout | **ELEVATED** |
| `helpdesk/tickets.py`, `store.py`, `priority.py`, `sla.py`, the tests, the Go CLI, the Java controller, the C tables, the web page and stylesheet | the plain business code — the scan does not fire on it | throughout | **NORMAL** |

Also in the report: six **agent artifacts** in the tree (an OpenClaw residue folder and its
gateway token at tier 3; a Claude Code workspace and an MCP config at tier 2; `CLAUDE.md`
and `.cursorrules` at tier 1), one **committed private key** (`agents/openclaw/deploy_key.pem`,
shown redacted), the **Build & Deployment Surface** (the Makefile and the workflow), the
**Agent Map**, and — from the report header — the Code Browser's Agents view and its
3-D Visualiser, with "Agent report" and "Metrics report" side by side.

Every figure above was produced by the tool on this folder. Nothing is hand-written.
