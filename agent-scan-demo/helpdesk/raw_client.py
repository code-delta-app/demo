"""SDK-less usage — calls an AI API directly over HTTP with no SDK import.

As of v1.8.2 Agent Scan catches this via known-endpoint detection: a raw POST to
a recognised model host (api.openai.com, api.anthropic.com, dashscope.aliyuncs.com,
...) is flagged even with no SDK import. Add your own hosts via codedelta_agents.json."""
import requests

def call_openai_raw(prompt, api_key):
    return requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"model": "gpt-4o", "messages": [{"role": "user", "content": prompt}]},
    ).json()

def call_anthropic_raw(prompt, api_key):
    return requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={"x-api-key": api_key},
        json={"model": "claude-opus-4-8", "max_tokens": 256,
              "messages": [{"role": "user", "content": prompt}]},
    ).json()
