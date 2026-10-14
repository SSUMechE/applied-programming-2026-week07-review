"""Supplied checks for the complete examples. There is no student test quota."""

from dataclasses import FrozenInstanceError
import json

# BEGIN SNIPPET test_imports
import numpy as np
import pytest

from functions_review import mm_to_m
# END SNIPPET test_imports
from objects_review import ReviewObstacle, Point, RadiusError, Scene


# BEGIN SNIPPET test_numeric
def test_mm_to_m_conversion():
    assert mm_to_m(12.5) == pytest.approx(0.0125, rel=1e-12, abs=1e-12)
    assert mm_to_m(0.0) == 0.0
# END SNIPPET test_numeric


# BEGIN SNIPPET test_invalid
def test_mm_to_m_negative_length():
    with pytest.raises(ValueError):
        mm_to_m(-1.0)
# END SNIPPET test_invalid


# BEGIN SNIPPET test_tolerance
def test_translation():
    points = np.array([[2., 4.], [6., 8.], [10., 12.]])
    actual = points + np.array([1., -2.])
    expected = np.array([[3., 2.], [7., 6.], [11., 10.]])
    assert actual.shape == expected.shape
    np.testing.assert_allclose(actual, expected, rtol=1e-12, atol=1e-12)
# END SNIPPET test_tolerance


@pytest.mark.parametrize("bad", [True, False, "12", None, np.nan, np.inf,
                                -np.inf, -1.0, 10**1000])
def test_mm_to_m_invalid_values(bad):
    with pytest.raises(ValueError):
        mm_to_m(bad)


@pytest.mark.parametrize("bad", [True, "0.5", None, 0.0, -1.0,
                                np.nan, np.inf, 10**1000])
def test_invalid_radius_preserves_existing_state(bad):
    obstacle = ReviewObstacle("post", (0.0, 0.0), 0.5)
    with pytest.raises(RadiusError):
        obstacle.resize(bad)
    assert obstacle.radius == 0.5


def test_radius_property_is_read_only_and_error_has_valueerror_base():
    obstacle = ReviewObstacle("post", (0.0, 0.0), 0.5)
    with pytest.raises(AttributeError):
        obstacle.radius = 1.0
    with pytest.raises(ValueError):
        obstacle.resize(0.0)


def test_same_instance_alias_and_scene_composition():
    first = ReviewObstacle("post", (0.0, 0.0), 0.5)
    second = ReviewObstacle("post", (0.0, 0.0), 0.5)
    alias = first
    alias.resize(0.75)
    assert first.radius == 0.75 and second.radius == 0.5
    source = [first, second]
    scene = Scene(source)
    source.pop()
    assert len(scene.obstacles) == 2
    assert scene.obstacles[0] is first


def test_frozen_point_owns_outer_sequence():
    source = [2.0, 4.0]
    point = Point(source)
    source[0] = 99.0
    assert point.values == (2.0, 4.0)
    assert point.count == 2
    assert point == Point((2.0, 4.0))
    with pytest.raises(FrozenInstanceError):
        point.values = (3.0, 4.0)
    with pytest.raises(ValueError):
        Point(())


def test_views_copies_axes_batch_and_interpolation():
    points = np.array([[2., 4.], [6., 8.], [10., 12.]])
    shared = points.copy()
    shared[1:2][0, 0] = 99.0
    independent = points.copy()
    copied = independent[1:2].copy()
    copied[0, 0] = 99.0
    np.testing.assert_array_equal(shared[1], [99.0, 8.0])
    np.testing.assert_array_equal(independent, points)
    np.testing.assert_allclose(points.sum(axis=1), [6., 14., 22.], rtol=1e-12, atol=1e-12)
    np.testing.assert_allclose(points.sum(axis=0), [18., 24.], rtol=1e-12, atol=1e-12)
    batch = np.array([points, points + [1., -2.]])
    assert batch.shape == (2, 3, 2)
    totals = np.sum(batch, axis=1)
    assert totals.shape == (2, 2)
    np.testing.assert_allclose(totals, [[18., 24.], [21., 18.]], rtol=1e-12, atol=1e-12)
    alpha = np.linspace(0.0, 1.0, 3)[:, None]
    samples = (1.0 - alpha) * points[0] + alpha * points[-1]
    np.testing.assert_allclose(samples, points, rtol=1e-12, atol=1e-12)


def test_json_text_is_not_an_obstacle():
    record = {"name": "marker", "center": [2.0, 0.0], "radius": 0.25}
    loaded = json.loads(json.dumps(record, allow_nan=False))
    assert isinstance(loaded, dict)
    restored = ReviewObstacle(loaded["name"], loaded["center"], loaded["radius"])
    assert restored.center == (2.0, 0.0)
    assert restored.radius == 0.25


def test_sampling_and_threshold_have_different_roles():
    minimums = []
    for count in (2, 9):
        x = np.linspace(-2.0, 2.0, count)
        minimums.append(float(np.min(np.abs(x) - 0.5)))
    np.testing.assert_allclose(minimums, [1.5, -0.5], rtol=1e-12, atol=1e-12)
    limits = np.array([0.5, 1.5, 1.6])
    margins = 1.5 - limits
    np.testing.assert_allclose(margins, [1.0, 0.0, -0.1], rtol=1e-12, atol=1e-12)
    np.testing.assert_array_equal(margins >= 0.0, [True, True, False])


def test_grid_is_cartesian_not_zipped_pairs():
    xs = np.linspace(-1.0, 1.0, 3)
    ys = np.linspace(-1.0, 1.0, 3)
    pairs = [(float(x), float(y)) for x in xs for y in ys]
    assert len(pairs) == len(set(pairs)) == 9
    assert pairs[0] == (-1.0, -1.0)
    assert pairs[-1] == (1.0, 1.0)
