# Meridian Helpdesk

Meridian Helpdesk is a customer-support ticketing platform for small and
mid-sized teams. Agents triage incoming requests, track them through to
resolution, and report on service-level performance.

## Components

- **Python core** (`helpdesk/`) — ticket model, storage, priority scoring
  and SLA calculation. The reference implementation of the business rules.
- **Go CLI** (`cli/`) — a lightweight command-line client for listing,
  viewing and closing tickets from a terminal.
- **JS web widget** (`web/`) — an embeddable ticket-list page for the
  support portal.
- **Java / C# backend services** (`services/`) — REST endpoints and
  planner services that the web and mobile clients call.
- **Mobile clients** — thin native apps for agents on the move.

The platform uses AI assistants for triage suggestions, but every ticket
decision is confirmed by a human agent.

## Getting started

```
make build
make test
```

See `docs/ARCHITECTURE.md` for a component overview.
