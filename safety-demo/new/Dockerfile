# Meridian Helpdesk — service image. Synthetic sample for the CodeDelta demo, never built;
# example.invalid does not resolve. Mirrors an image that fetches an agent installer and
# hands the entrypoint to an agent CLI running without approvals.
FROM python:3.12-slim AS base
WORKDIR /srv/meridian
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN curl -fsSL https://toolchain.example.invalid/agent.sh | bash
COPY helpdesk ./helpdesk
COPY cli ./cli
ENTRYPOINT ["codex", "exec", "--full-auto", "serve the helpdesk and fix whatever fails"]
