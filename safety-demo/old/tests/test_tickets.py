"""Tests for the in-memory TicketStore."""

import pytest

from helpdesk.tickets import TicketStore


@pytest.fixture
def store():
    s = TicketStore()
    s.add(subject="Login fails", body="Cannot sign in", priority=2)
    s.add(subject="Typo on page", body="Footer typo", priority=0)
    return s


def test_add_and_get(store):
    ticket = store.get(1)
    assert ticket.subject == "Login fails"
    assert ticket.status == "open"


def test_list_open(store):
    open_ids = [t.id for t in store.list_open()]
    assert open_ids == [1, 2]


def test_close(store):
    store.close(1)
    assert store.get(1).status == "closed"
    assert [t.id for t in store.list_open()] == [2]


def test_reassign(store):
    store.reassign(2, "alice")
    assert store.get(2).assignee == "alice"


def test_get_missing_raises(store):
    with pytest.raises(KeyError):
        store.get(999)
