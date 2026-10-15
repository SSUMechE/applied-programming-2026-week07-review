"""Four independent chapter-practice tests, not Assignment 3 evidence tests.

These tests exercise only the simplified PracticeHistory contract.
Their count and cases add no assignment completion or assessment requirement.
"""

import pytest

from practice_history import PracticeHistory


def test_normal_record_keeps_order_and_returns_a_snapshot():
    history = PracticeHistory()
    history.record("first attempt")
    snapshot = history.results
    history.record("second attempt")

    assert snapshot == ("first attempt",)
    assert history.results == ("first attempt", "second attempt")
    assert isinstance(history.results, tuple)


def test_invalid_non_string_label_is_rejected():
    history = PracticeHistory()

    with pytest.raises(ValueError):
        history.record(123)


def test_two_instances_have_independent_histories():
    first = PracticeHistory()
    second = PracticeHistory()
    first.record("first attempt")

    assert first.results == ("first attempt",)
    assert second.results == ()


def test_rejected_update_leaves_existing_history_unchanged():
    history = PracticeHistory()
    history.record("valid attempt")
    before = history.results

    with pytest.raises(ValueError):
        history.record("   ")

    assert history.results == before
