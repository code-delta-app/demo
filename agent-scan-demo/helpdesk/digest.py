"""Demonstrates the v1.8.x cost + data-sovereignty signals.

- The classify loop calls an AI model once per row with no rate limit or cap:
  cost_risk(ai_calls_inside_loop) — a runaway-API-bill pattern.
- It uses DeepSeek (api.deepseek.com / dashscope), a China-hosted model:
  data_egress(model_hosted_in_CN:...) + data_sovereignty_risk — your prompts
  (and any data in them) leave the country.
"""
import requests


def classify_rows(rows, api_key):
    results = []
    for row in rows:                      # <-- AI call inside a loop = cost risk
        resp = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={"model": "deepseek-chat",
                  "messages": [{"role": "user", "content": row["text"]}]},
        )
        results.append(resp.json())
    return results
