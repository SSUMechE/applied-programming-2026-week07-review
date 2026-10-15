import pytest

def wrong_distance(start, goal):
    return abs(goal[0] - start[0]) + abs(goal[1] - start[1])

def test_wrong_distance():
    actual = wrong_distance((0.0, 0.0), (3.0, 4.0))
    assert actual == pytest.approx(5.0, rel=1e-12, abs=1e-12)
