"""Routine AI integration — imports SDKs and makes ordinary model calls.
Agent Scan should rate this ELEVATED: it clearly uses AI, but does nothing risky."""
import openai
from anthropic import Anthropic

def ask_openai(question: str) -> str:
    client = openai.OpenAI()
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": question}],
    )
    return resp.choices[0].message.content

def ask_claude(question: str) -> str:
    client = Anthropic()
    msg = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=512,
        messages=[{"role": "user", "content": question}],
    )
    return msg.content[0].text

def ask_with_fallback(question: str) -> str:
    """Ask OpenAI first; fall back to Claude if the primary call fails."""
    try:
        return ask_openai(question)
    except Exception:
        return ask_claude(question)
