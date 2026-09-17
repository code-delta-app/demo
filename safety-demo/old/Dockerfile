# Meridian Helpdesk — service image (helpdesk/ + cli/)
FROM python:3.12-slim AS base
WORKDIR /srv/meridian
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY helpdesk ./helpdesk
COPY cli ./cli
USER nobody
ENTRYPOINT ["python", "-m", "helpdesk"]
