# Meridian Helpdesk — Architecture

Meridian Helpdesk is organised around a small Python core that owns the
business rules, with thin clients in other languages calling into the same
concepts.

## Components

- **helpdesk/** — Python core: the `Ticket` model and `TicketStore`
  (in-memory), a SQLite persistence wrapper, priority scoring and SLA
  deadline calculation.
- **cli/** — a Go command-line client (`list`, `show`, `close`).
- **web/** — a static ticket-list page for the support portal.
- **services/** — Java (Spring-style REST) and C# planner services that
  the web and mobile clients call.

## Data flow

1. A request arrives through the web widget or a backend service.
2. The core scores its priority and computes an SLA deadline.
3. The ticket is stored and surfaced to agents, newest and highest
   priority first.

## Typical usage

```python
from helpdesk.tickets import TicketStore

store = TicketStore()
tid = store.add(subject="Login fails", body="Cannot sign in", priority=2)
ticket = store.get(tid)
print(ticket.status)          # "open"

store.close(tid)
print([t.id for t in store.list_open()])
```
