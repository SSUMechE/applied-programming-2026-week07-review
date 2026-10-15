import pytest
from learning_geometry import distance_example, PathInputError

def test_normal_distance():
    actual = distance_example((0.0, 0.0), (3.0, 4.0))
    assert actual == pytest.approx(5.0, rel=1e-12, abs=1e-12)

def test_zero_length():
    assert distance_example((2.0, 1.0), (2.0, 1.0)) == 0.0

def test_invalid_point():
    with pytest.raises(PathInputError):
        distance_example((0.0, 0.0), (True, 4.0))
