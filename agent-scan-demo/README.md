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
| `rogue_executor.py` | `exec`/`eval` on model output | **HIGH/CRITICAL** — the "rogue agent" pattern |
| `unsafe_prompt.py` | Untrusted `input()` flows into prompts | **ELEVATED** + injection vectors |
| `frontend.js` | JavaScript OpenAI/Anthropic SDKs | flagged (JS is supported) |
| `plain_utils.py` | No AI usage at all (control) | **NORMAL**, not flagged |
| `chinese_models.py` | DeepSeek / Qwen / Zhipu GLM | **ELEVATED** — native `dashscope` + `zhipuai` now detected (v1.8.2) |
| `raw_http.py` | Raw HTTP to an AI endpoint, no SDK | **ELEVATED** — known-endpoint detection now catches it (v1.8.2) |
| `cost_and_sovereignty.py` | AI call in a loop + China-hosted model | **HIGH** — `cost_risk` (runaway API bill) + `data_egress(CN)` + `data_sovereignty_risk` |
| `model_gateway.go` | Go: raw HTTP to OpenAI, no SDK | **ELEVATED** — known-endpoint detection is language-agnostic (Go too) |
| `sovereign_router.go` | Go: routes prompts to Qwen + DeepSeek (CN) | **ELEVATED** — `data_egress(CN)` + `data_sovereignty_risk` from a Go service |

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
