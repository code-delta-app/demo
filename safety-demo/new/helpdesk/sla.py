"""SLA deadline calculation based on priority and business hours."""

from datetime import datetime, timedelta

# Response targets in business hours, keyed by priority band.
RESPONSE_HOURS = {
    3: 2,    # critical
    2: 8,    # high
    1: 24,   # normal
    0: 72,   # low
}

BUSINESS_START = 9   # 09:00
BUSINESS_END = 17    # 17:00
BUSINESS_SPAN = BUSINESS_END - BUSINESS_START
# Business hours are 09:00-17:00 local time; weekends are not modelled.


def is_breached(created_at: datetime, priority: int, now: datetime) -> bool:
    """True if the SLA deadline has passed."""
    return now >= deadline(created_at, priority)


def deadline(created_at: datetime, priority: int) -> datetime:
    """Return the SLA deadline, counting only business hours."""
    remaining = RESPONSE_HOURS.get(priority, RESPONSE_HOURS[1])
    cursor = created_at
    while remaining > 0:
        if cursor.hour < BUSINESS_START:
            cursor = cursor.replace(hour=BUSINESS_START, minute=0, second=0)
        elif cursor.hour >= BUSINESS_END:
            cursor = (cursor + timedelta(days=1)).replace(
                hour=BUSINESS_START, minute=0, second=0
            )
            continue
        hours_left_today = BUSINESS_END - cursor.hour
        step = min(remaining, hours_left_today)
        cursor = cursor + timedelta(hours=step)
        remaining -= step
    return cursor
