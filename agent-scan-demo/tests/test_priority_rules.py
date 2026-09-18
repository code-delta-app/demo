"""Priority rules: keyword bands and age escalation."""
from helpdesk.priority import score_priority, is_escalated


def test_keyword_sets_the_band():
    assert score_priority("Site is down", "") == 3
    assert score_priority("Small typo", "") == 0


def test_age_escalates():
    assert score_priority("Slow page", "", age_hours=30) == 2
    assert score_priority("Slow page", "", age_hours=80) == 3


def test_is_escalated():
    assert is_escalated("Outage in EU", "")
    assert not is_escalated("Question about billing", "")
