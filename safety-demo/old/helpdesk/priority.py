"""Priority scoring from keywords and ticket age."""

# Keyword weights: higher means more urgent.
KEYWORD_WEIGHTS = {
    "down": 3,
    "outage": 3,
    "urgent": 2,
    "fails": 2,
    "error": 1,
    "slow": 1,
}

MAX_SCORE = 3


def score_priority(subject: str, body: str, age_hours: float = 0.0) -> int:
    """Return an integer priority band in the range 0..3."""
    text = f"{subject} {body}".lower()
    raw = 0
    for keyword, weight in KEYWORD_WEIGHTS.items():
        if keyword in text:
            raw = max(raw, weight)

    # Older unresolved tickets escalate.
    if age_hours >= 48:
        raw += 1

    return max(0, min(MAX_SCORE, raw))
