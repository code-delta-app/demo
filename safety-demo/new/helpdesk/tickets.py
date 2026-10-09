"""In-memory ticket model and store."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional


@dataclass
class Ticket:
    id: int
    subject: str
    body: str
    status: str = "open"
    priority: int = 0
    created_at: datetime = field(default_factory=datetime.utcnow)
    assignee: Optional[str] = None


class TicketStore:
    """A dict-backed collection of tickets."""

    def __init__(self) -> None:
        self._tickets: Dict[int, Ticket] = {}
        self._next_id = 1

    def add(self, subject: str, body: str, priority: int = 0) -> int:
        ticket = Ticket(
            id=self._next_id, subject=subject, body=body, priority=priority
        )
        self._tickets[ticket.id] = ticket
        self._next_id += 1
        return ticket.id

    def get(self, ticket_id: int) -> Ticket:
        return self._tickets[ticket_id]

    def list_open(self) -> List[Ticket]:
        return [t for t in self._tickets.values() if t.status == "open"]

    def close(self, ticket_id: int) -> None:
        ticket = self._tickets[ticket_id]
        if ticket.status == "closed":
            return
        ticket.status = "closed"
        ticket.closed_at = datetime.utcnow()

    def reassign(self, ticket_id: int, assignee: str) -> None:
        ticket = self._tickets[ticket_id]
        ticket.assignee = assignee
