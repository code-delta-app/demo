"""Small date helpers used across the core."""

from datetime import datetime, timedelta


def business_days_between(start: datetime, end: datetime) -> int:
    """Count weekdays between two datetimes (inclusive of start day)."""
    if end < start:
        start, end = end, start
    days = 0
    cursor = start
    while cursor.date() <= end.date():
        if cursor.weekday() < 5:
            days += 1
        cursor += timedelta(days=1)
    return days


def add_hours(when: datetime, hours: float) -> datetime:
    """Return a new datetime offset by the given hours."""
    return when + timedelta(hours=hours)
