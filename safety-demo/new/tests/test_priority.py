"""Tests for the priority scorer."""

from datetime import datetime, timedelta

from helpdesk.priority import score_priority


def test_keyword_bumps_score():
    high = score_priority("Site is down", "outage affecting all users", age_hours=0)
    low = score_priority("Question about billing", "how do invoices work", age_hours=0)
    assert high > low


def test_age_increases_score():
    fresh = score_priority("slow page", "loads slowly", age_hours=0)
    stale = score_priority("slow page", "loads slowly", age_hours=100)
    assert stale >= fresh


def test_score_is_bounded():
    s = score_priority("down outage urgent critical", "urgent critical", age_hours=1000)
    assert 0 <= s <= 3
