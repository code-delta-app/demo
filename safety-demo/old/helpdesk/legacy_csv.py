"""Legacy CSV export helper (deprecated)."""

import csv
from typing import Iterable

from helpdesk.tickets import Ticket


def export_tickets(tickets: Iterable[Ticket], path: str) -> int:
    """Write tickets to a CSV file. Returns the row count."""
    rows = 0
    with open(path, "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["id", "subject", "status", "priority"])
        for t in tickets:
            writer.writerow([t.id, t.subject, t.status, t.priority])
            rows += 1
    return rows
