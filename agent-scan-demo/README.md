# Meridian Helpdesk — the Agent Scan demo

A fictional customer-support product: a Python core, a Go CLI, a web widget, Java and C#
services, a C++ gateway, mobile clients, analytics in R, Julia and Scala, edge scripts in Lua,
integrations in Elixir and Ruby, an ops toolkit in Perl and PowerShell, a Rust indexer and a CI
pipeline — 90 files across 27 languages and file types. Every one of them is inert:
nothing here contacts a model or runs anything. Thirty-one of them are written in the exact
shape of the ways AI has been abused inside real software. Agent Scan finds each one and says which.

Run it from the app: **Try It — Demos → Agent Scan Demo → Run**, or from the command line
on the folder the app downloaded:

```bash
codedelta-gui scan <folder> --mode agent
```

Expected: **31 CRITICAL, 2 HIGH, 28 ELEVATED, 29 NORMAL** of 90 files.
The report's summary line, as the tool prints it:

> 32 file(s) run what a model tells them, across 26 languages and file types — the rogue agent pattern (eval/exec or a process launch near an AI call); 2 launch an AI agent with its permission checks off; 1 hide their instructions to a model in encoded strings; 5 send data to models hosted in a sovereignty-sensitive jurisdiction; 1 talk to a model running on the local machine. Scanned 90 file(s): 31 CRITICAL, 2 HIGH, 28 ELEVATED. 4 file(s) carry a base64 literal that decodes to AI-calling source (encoded payload). AI SDKs detected: llama.h, ollama_rs::, async_openai::, http:api.openai.com. 2 tier-3 agent artifact(s) in the tree (rogue-agent residue / committed credentials). Coverage: 74 file(s) with full language rules, 2 at endpoint level (shell/CI recipes and Objective-C: endpoint and launch rules), 14 at text-level (endpoints, encoded payloads and dangerous Markdown code blocks; ELEVATED at most). 

"Start here" under it links the three highest-scoring cards: `analytics/julia/ops_helper.jl`, `analytics/r/report_gen.R`, `analytics/scala/src/main/scala/BatchOps.scala`.

## CRITICAL — 31 cards, one per file

| File | What it mirrors | Language | Rated |
|---|---|---|---|
| `analytics/julia/ops_helper.jl` | Julia: an ops helper that runs the command the model wrote | Julia | **CRITICAL** (AIS 100) |
| `analytics/r/report_gen.R` | R: a report generator that runs the model's `system()` suggestion | R | **CRITICAL** (AIS 100) |
| `analytics/scala/src/main/scala/BatchOps.scala` | Scala: batch operations executed from a model reply | Scala | **CRITICAL** (AIS 100) |
| `build-tools/AutoPatch.groovy` | Groovy build tool: a patch asked of the model and applied by a process launch | Groovy | **CRITICAL** (AIS 100) |
| `edge/nginx/lua/dynamic_route.lua` | Lua inside nginx: routing decisions fetched from a model and executed at the edge | Lua | **CRITICAL** (AIS 100) |
| `helpdesk/autofix.py` | the classic: `exec` on model output | Python | **CRITICAL** (AIS 100) |
| `helpdesk/local_assistant.py` | PromptLock (Aug 2025): a model running on the local machine — reached through the Ollama library, no address anywhere in the file — whose reply is executed | Python | **CRITICAL** (AIS 100) |
| `helpdesk/telemetry/beacon.py` | an AI-calling program hidden as a base64 string and executed | Python | **CRITICAL** (AIS 100) |
| `helpdesk/telemetry/beacon_gz.py` | the same agent compressed, then base64, then executed — the third encoding layer | Python | **CRITICAL** (AIS 100) |
| `helpdesk/telemetry/beacon_hex.py` | the same agent as a hex string, run via `bytes.fromhex` — the second encoding the scanner decodes | Python | **CRITICAL** (AIS 100) |
| `helpdesk/telemetry/update_check.py` | LameHug (Jul 2025): the instructions to the model hidden as a base64 string, sent to a hosted model, the reply run as a command | Python | **CRITICAL** (AIS 100) |
| `integrations/elixir/lib/runbook.ex` | Elixir: a runbook step asked of the model and run with `System.cmd` | Elixir | **CRITICAL** (AIS 100) |
| `integrations/ruby/lib/deploy_hook.rb` | Ruby: a deploy hook that runs whatever the model suggests | Ruby | **CRITICAL** (AIS 100) |
| `mobile/android/app/src/main/kotlin/com/meridian/Assistant.kt` | Kotlin: the model's reply handed to a process launcher | Kotlin | **CRITICAL** (AIS 100) |
| `mobile/flutter/lib/auto_reply.dart` | Dart: the same in Flutter | Dart | **CRITICAL** (AIS 100) |
| `mobile/ios/Meridian/Chat.swift` | Swift: the same on iOS | Swift | **CRITICAL** (AIS 100) |
| `native/audio/voice_cmd.c` | C: a local llama model transcribes a voice command and the text is run as a shell command | C | **CRITICAL** (AIS 100) |
| `native/gateway/ModelGateway.cpp` | C++: a raw HTTP call to a model, `system()` on the reply | C++ | **CRITICAL** (AIS 100) |
| `native/indexer/src/maintenance.rs` | Rust: a model reply passed to `Command::new` — maintenance driven by the model | Rust | **CRITICAL** (AIS 100) |
| `notebooks/explore.ipynb` | a notebook whose third cell `exec`s what the model returned — the finding names the line and the cell | Jupyter notebook | **CRITICAL** (AIS 100) |
| `ops/perl/log_triage.pl` | Perl: log triage where the model's fix is passed to `system` | Perl | **CRITICAL** (AIS 100) |
| `ops/windows/Invoke-AutoFix.ps1` | PowerShell: `Invoke-Expression` on the model's answer | PowerShell | **CRITICAL** (AIS 100) |
| `scripts/bootstrap.sh` | the same shape in shell: `OLLAMA_HOST`, `ollama run`, `eval` of the reply | Shell | **CRITICAL** (AIS 100) |
| `services/java/src/main/java/com/meridian/OpenAiAssistant.java` | Java: whatever the model returns is run as a shell command | Java | **CRITICAL** (AIS 100) |
| `services/planner/KernelPlanner.cs` | C#: Semantic Kernel planner output handed straight to the operating system | C# | **CRITICAL** (AIS 100) |
| `web/php/auto_action.php` | PHP: `shell_exec` of a model reply on the server | PHP | **CRITICAL** (AIS 100) |
| `web/src/autoResolve.ts` | TypeScript: ticket auto-resolution that `eval`s the model's code | JavaScript | **CRITICAL** (AIS 100) |
| `web/src/components/AssistantPanel.vue` | a Vue component doing the same inside the front end | Vue | **CRITICAL** (AIS 100) |
| `web/widget.html` | a page that `fetch`es a model and `eval`s the reply in the browser | HTML | **CRITICAL** (AIS 100) |
| `.github/workflows/autofix.yml` | a CI recipe running `codex exec` with approvals bypassed on every push | CI recipe | **CRITICAL** (AIS 70) |
| `build/postinstall.js` | The nx "s1ngularity" supply-chain attack (Aug 2025): a post-install script that launches the developer's own Claude and Gemini command-line agents with their safety checks switched off | JavaScript | **CRITICAL** (AIS 70) |

## HIGH — 2

| File | What it mirrors | Language | Rated |
|---|---|---|---|
| `helpdesk/digest.py` | a model called inside a loop, and the model is hosted in China | Python | **HIGH** (AIS 98) |
| `helpdesk/crew.py` | LangChain + CrewAI: autonomous crews spun up from code | Python | **HIGH** (AIS 80) |

## ELEVATED — 28: ordinary AI use (an SDK import, a model call, the reply printed), sovereignty and documentation findings

| File | What it mirrors | Language | Rated |
|---|---|---|---|
| `docs/RUNBOOK.md` | Incident runbook | text (.md) | **ELEVATED** (AIS 60) |
| `cli/internal/gateway/router.go` | sovereign_router.go — routes prompts to non-Western model hosts. | Go | **ELEVATED** (AIS 58) |
| `helpdesk/prompts.py` | User input flows straight into the prompt — classic injection surface. | Python | **ELEVATED** (AIS 58) |
| `helpdesk/providers/cn.py` | DeepSeek via its OpenAI-compatible endpoint — detected via the openai import. | Python | **ELEVATED** (AIS 58) |
| `helpdesk/raw_client.py` | ai_http_endpoint(api.openai.com) | Python | **ELEVATED** (AIS 58) |
| `helpdesk/triage.py` | ai_sdk_import(3_sdk(s)_detected) | Python | **ELEVATED** (AIS 58) |
| `analytics/julia/sentiment.jl` | ai_sdk_import(1_sdk(s)_detected) | Julia | **ELEVATED** (AIS 40) |
| `analytics/r/csat_model.R` | ai_sdk_import(1_sdk(s)_detected) | R | **ELEVATED** (AIS 40) |
| `analytics/scala/src/main/scala/Classifier.scala` | ai_sdk_import(1_sdk(s)_detected) | Scala | **ELEVATED** (AIS 40) |
| `build-tools/QualityCheck.groovy` | ai_sdk_import(1_sdk(s)_detected) | Groovy | **ELEVATED** (AIS 40) |
| `cli/internal/gateway/model_gateway.go` | model_gateway.go — SDK-less AI access in Go. | Go | **ELEVATED** (AIS 40) |
| `edge/nginx/lua/route_hint.lua` | ai_sdk_import(1_sdk(s)_detected) | Lua | **ELEVATED** (AIS 40) |
| `helpdesk/providers/ru.py` | Raw HTTP, no SDK — caught by known-endpoint detection. | Python | **ELEVATED** (AIS 40) |
| `helpdesk/telemetry/beacon_disabled.py` | The same agent, encoded, but this file never executes it. | Python | **ELEVATED** (AIS 40) |
| `integrations/elixir/lib/summarizer.ex` | ai_sdk_import(1_sdk(s)_detected) | Elixir | **ELEVATED** (AIS 40) |
| `integrations/ruby/lib/slack_bot.rb` | ai_sdk_import(1_sdk(s)_detected) | Ruby | **ELEVATED** (AIS 40) |
| `mobile/flutter/lib/assistant.dart` | ai_sdk_import(1_sdk(s)_detected) | Dart | **ELEVATED** (AIS 40) |
| `native/audio/transcribe.c` | include "llama.h" | C | **ELEVATED** (AIS 40) |
| `native/gateway/ModelGateway.hpp` | pragma once | C++ | **ELEVATED** (AIS 40) |
| `native/indexer/src/embed.rs` | ai_sdk_import(1_sdk(s)_detected) | Rust | **ELEVATED** (AIS 40) |
| `native/llama/infer.cpp` | include "llama.h" | C++ | **ELEVATED** (AIS 40) |
| `ops/perl/digest.pl` | ai_sdk_import(1_sdk(s)_detected) | Perl | **ELEVATED** (AIS 40) |
| `ops/windows/Get-TicketSummary.ps1` | ai_sdk_import(1_sdk(s)_detected) | PowerShell | **ELEVATED** (AIS 40) |
| `services/java/src/main/java/com/meridian/SupportAgent.java` | An AI call inside a loop: one ticket, one model round-trip, no cap on the bill. | Java | **ELEVATED** (AIS 40) |
| `services/planner/AzureChat.cs` | ai_sdk_import(1_sdk(s)_detected) | C# | **ELEVATED** (AIS 40) |
| `web/app.js` | JavaScript/TypeScript AI usage — Agent Scan covers JS SDKs too. | JavaScript | **ELEVATED** (AIS 40) |
| `web/php/ticket_summary.php` | ai_sdk_import(1_sdk(s)_detected) | PHP | **ELEVATED** (AIS 40) |
| `web/src/assistant.ts` | ai_sdk_import(1_sdk(s)_detected) | JavaScript | **ELEVATED** (AIS 40) |

## NORMAL — 29

The plain business code: tickets, store, priority and SLA modules, the tests, the Go CLI's
store, the Java ticket controller, the C tables, the web page and stylesheet, the build files.
The scan does not fire on it.

## Also in the report

Six **agent artifacts** in the tree (an OpenClaw residue folder and its gateway token at tier 3;
a Claude Code workspace and an MCP config at tier 2; `CLAUDE.md` and `.cursorrules` at tier 1),
one **committed private key** (`agents/openclaw/deploy_key.pem`, shown redacted), the **Build &
Deployment Surface** (the Makefile and the workflow), **data sovereignty** (four files sending
data to models hosted in China, one to Russia), **cost risk** (a model called inside a loop), the
**AI SDK inventory** (35 SDKs and endpoints), the **Agent Map**, and — from the report header —
the Code Browser's Agents view and its 3-D Visualiser, with "Agent report" and "Metrics report"
side by side.

Every figure above was produced by the tool on this folder. Nothing is hand-written.
