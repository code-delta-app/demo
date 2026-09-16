"""SQLite-backed persistence for tickets."""

# Standard-library only: no ORM.
import sqlite3
from typing import List, Optional, Tuple


class SqliteStore:
    """A tiny SQLite wrapper for ticket rows."""

    def __init__(self, path: str = ":memory:") -> None:
        self.conn = sqlite3.connect(path)
        # Rows come back as sqlite3.Row so columns are addressable by name.
        self.conn.row_factory = sqlite3.Row

    def create_table(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                subject TEXT NOT NULL,
                body TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'open',
                priority INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        self.conn.commit()

    def insert_ticket(self, subject: str, body: str, priority: int = 0) -> int:
        cur = self.conn.execute(
            "INSERT INTO tickets (subject, body, priority) VALUES (?, ?, ?)",
            (subject, body, priority),
        )
        self.conn.commit()
        return int(cur.lastrowid)

    def fetch_ticket(self, ticket_id: int) -> Optional[sqlite3.Row]:
        cur = self.conn.execute(
            "SELECT * FROM tickets WHERE id = ?", (ticket_id,)
        )
        return cur.fetchone()

    # TODO: add an index on status.
    def all_open(self) -> List[sqlite3.Row]:
        cur = self.conn.execute(
            "SELECT * FROM tickets WHERE status = 'open' ORDER BY priority DESC"
        )
        return cur.fetchall()

    def close(self) -> None:
        self.conn.close()
