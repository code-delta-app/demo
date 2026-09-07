# Agent Scan demo

A small project that exercises CodeDelta's **Agent Scan** — the scan that finds
code which *uses* AI (calls or runs an AI model at runtime), as opposed to code
that was *written by* AI.

Run it:

```bash
python3 codedelta_server.py scan examples/agent-scan-demo --mode agent --html
```

## What each file demonstrates

| File | Demonstrates | Expected |
|------|--------------|----------|
| `chatbot.py` | Routine OpenAI + Anthropic calls | **ELEVATED** — uses AI, nothing risky |
| `multi_agent.py` | LangChain + CrewAI agent orchestration | **ELEVATED/HIGH** — agent initiation |
| `rogue_executor.py` | `exec`/`eval` on model output | **CRITICAL** — the "rogue agent" pattern |
| `unsafe_prompt.py` | Untrusted `input()` flows into prompts | **ELEVATED** + injection vectors |
| `frontend.js` | JavaScript OpenAI/Anthropic SDKs | flagged (JS is supported) |
| `plain_utils.py` | No AI usage at all (control) | **NORMAL**, not flagged |
| `java/OpenAiAssistant.java` | Java OpenAI SDK; model output handed to `Runtime.exec` | **CRITICAL** — SDK import + rogue-agent pattern (class `OpenAiAssistant`) |
| `java/SupportAgent.java` | LangChain4j + OpenAI; extends `OpenAiAssistant`; AI call in a loop | **ELEVATED** — SDK imports |
| `csharp/KernelPlanner.cs` | Semantic Kernel planner; `kernel.add_plugin`; plan handed to `Process.Start` | **CRITICAL** — SDK import + agent orchestration + rogue-agent pattern |
| `csharp/AzureChat.cs` | Azure OpenAI client class | **ELEVATED** — SDK import |
| `cpp/ModelGateway.hpp` | `ModelGateway` base with `OpenAiGateway` / `DeepSeekGateway` subclasses; raw endpoints | **ELEVATED** — endpoint + data egress CN + sovereignty |
| `cpp/ModelGateway.cpp` | libcurl POST to a known endpoint, `popen` on the reply | **CRITICAL** — endpoint + rogue-agent pattern |
| `chinese_models.py` | DeepSeek / Qwen / Zhipu GLM | **ELEVATED** — native `dashscope` + `zhipuai` now detected (v1.8.2) |
| `raw_http.py` | Raw HTTP to an AI endpoint, no SDK | **ELEVATED** — known-endpoint detection now catches it (v1.8.2) |
| `cost_and_sovereignty.py` | AI call in a loop + China-hosted model | **HIGH** — `cost_risk` (runaway API bill) + `data_egress(CN)` + `data_sovereignty_risk` |
| `model_gateway.go` | Go: raw HTTP to OpenAI, no SDK | **ELEVATED** — known-endpoint detection is language-agnostic (Go too) |
| `sovereign_router.go` | Go: routes prompts to Qwen + DeepSeek (CN) | **ELEVATED** — `data_egress(CN)` + `data_sovereignty_risk` from a Go service |
| `russian_models.py` | Sber GigaChat + YandexGPT (native SDKs + raw HTTP) | **ELEVATED** — `data_egress(RU)` + `data_sovereignty_risk` (native RU detection, v1.9.1) |
| `encoded/hidden_agent_executed.py` | OpenAI agent base64-encoded in a string, `exec(b64decode(...))` | **CRITICAL** — encoded payload decoded and found, and the file runs it |
| `encoded/hidden_in_hex.py` | Same agent as a hex string, `exec(bytes.fromhex(...))` | **CRITICAL** — hex layer decoded |
| `encoded/hidden_gzip_base64.py` | Same agent gzip-compressed, then base64, then executed | **CRITICAL** — compression layer undone |
| `encoded/hidden_agent_not_run.py` | Encoded OpenAI call that the file never executes | **ELEVATED** — hidden AI code reported, not run |
| `encoded/just_a_logo.py` | A base64 PNG, the ordinary embedded image | **NORMAL** — dropped by signature, never scanned |


## Agent Infrastructure samples (v1.9.1)

The tree also carries **inert agent artifacts** so the report's Agent
Infrastructure section has something to show — evidence that an agent
*operates on* a repo, as opposed to code that calls AI:

| Artifact | Tier | Expected |
|----------|------|----------|
| `CLAUDE.md`, `.cursorrules` | 1 | counted as sanctioned agent-assisted development |
| `.claude/` workspace, `.mcp.json` | 2 | listed — an agent runs against this repo |
| `openclaw/` directory | 3 | listed with full path — rogue-agent residue |
| `openclaw/gateway.auth.token` | 3 | listed, noted as **empty placeholder** (it is exactly that — an empty file) |

Every artifact here is inert: empty or a stub JSON that configures nothing.
Tier-3 findings never fail a build unless `"fail_on_agent_artifacts": true`
is set in a `--gate-policy` file.

## Encoded payloads (added 7 Sep 2026)

The `encoded/` folder shows the agent scan's second pass over encoded literals.
Each file hides the same OpenAI agent inside a string — base64, hex, or gzip
then base64 — and three of them execute it. With **decode encoded literals**
on (the default), the hidden code is decoded, scanned like a file, and the
host is rated CRITICAL when it runs what it decoded. With the pass off, those
files show only "dynamic execution" (ELEVATED) and the hidden call is
invisible. The PNG file proves images are dropped at once. All payloads are
inert: nothing here is ever executed and there is no API key.


## Fixed in v1.8.2

- **Non-Western native SDKs now recognised** — `dashscope` (Qwen), `zhipuai`
  (GLM), `qianfan` (ERNIE), `moonshot` (Kimi), `deepseek`, plus more Western
  providers (replicate, huggingface_hub, fireworks, perplexity, ai21, …).
- **Using an AI SDK now reaches ELEVATED on its own** — a clean integration
  (e.g. `frontend.js`) is no longer under-reported as NORMAL.
- **SDK-less HTTP calls now caught** — a raw POST to a known model endpoint
  (`api.openai.com`, `dashscope.aliyuncs.com`, …) is flagged even with no SDK
  import (`raw_http.py`).
- **User-extensible providers** — drop a `codedelta_agents.json` (see
  `codedelta_agents.example.json`) to add your own AI SDK import names and API
  endpoints, additive on top of the built-ins, no release needed.

## Remaining roadmap

- **Cost / data-sovereignty signals** — e.g. "AI call inside a loop" (runaway
  cost) and "calls a foreign-hosted model" (compliance/data-residency).

## Classes (added 7 Sep 2026)

The Java, C# and C++ files exist so the Code Browser has classes to show for this
demo: `SupportAgent extends OpenAiAssistant`, `OpenAiGateway` and `DeepSeekGateway`
inherit `ModelGateway`, plus `KernelPlanner`, `ShellPlugin` and `AzureChat`. Measured on
CodeDelta 2.0.1 (7 Sep 2026, rogue-agent check extended to every scanned language): 23 files scanned, 21 flagged, 7 CRITICAL, 2 HIGH, 12 ELEVATED (a rogue-agent file is CRITICAL since 7 Sep 2026);
Classes tab lists 7 classes. All files are synthetic and never executed.
