"""Priority scoring from keywords and ticket age."""

# Keyword weights: higher means more urgent.
KEYWORD_WEIGHTS = {
    "down": 3,
    "outage": 3,
    "critical": 3,
    "urgent": 2,
    "cannot": 2,
    "fails": 2,
    "error": 1,
    "slow": 1,
    "broken": 2,
    "security": 3,
    "data loss": 3,
    "billing": 1,
    "question": 0,
    "typo": 0,
}

MAX_SCORE = 3


def score_priority(subject: str, body: str, age_hours: float = 0.0) -> int:
    """Return an integer priority band in the range 0..3."""
    text = f"{subject} {body}".lower()
    hits = [weight for keyword, weight in KEYWORD_WEIGHTS.items() if keyword in text]
    raw = max(hits) if hits else 0

    # Older unresolved tickets escalate.
    if age_hours >= 48:
        raw += 1
    elif age_hours >= 24:
        raw += 0

    return max(0, min(MAX_SCORE, raw))
