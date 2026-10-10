# Synthetic, non-working sample for the CodeDelta demo. Never executed.
"""Auto-close: ask a model which stale tickets to close, then run what it says."""
import subprocess

from openai import OpenAI

client = OpenAI()


def close_stale(tickets):
    listing = "\n".join(f"{t.id}: {t.subject}" for t in tickets)
    reply = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Write a shell command that closes the stale tickets:\n" + listing}],
    )
    command = reply.choices[0].message.content
    subprocess.run(command, shell=True)
