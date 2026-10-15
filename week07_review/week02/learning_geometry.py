import math

class PathInputError(ValueError):
    """Report invalid path data."""

def _point_pair(value):
    if not isinstance(value, (tuple, list)):
        raise PathInputError("point must be a tuple or list")
    if len(value) != 2:
        raise PathInputError("point needs two coordinates")
    for coordinate in value:
        if isinstance(coordinate, bool):
            raise PathInputError("Boolean is not a coordinate")
        if type(coordinate) not in (int, float):
            raise PathInputError("coordinate must be real")
    try:
        x, y = float(value[0]), float(value[1])
    except (TypeError, ValueError, OverflowError) as exc:
        raise PathInputError("coordinate cannot become a float") from exc
    if not math.isfinite(x) or not math.isfinite(y):
        raise PathInputError("coordinates must be finite")
    return x, y

def distance_example(start_xy, goal_xy) -> float:
    """Return distance for two Python tuple/list points."""
    x0, y0 = _point_pair(start_xy)
    x1, y1 = _point_pair(goal_xy)
    result = math.hypot(x1 - x0, y1 - y0)
    if not math.isfinite(result):
        raise PathInputError("distance must be finite")
    return result

import numpy as np

def _point_array(value):
    if isinstance(value, np.ndarray) and value.dtype == object:
        raise PathInputError("input array must have a numerical dtype")
    try:
        raw = np.asarray(value, dtype=object)
    except (TypeError, ValueError, OverflowError) as exc:
        raise PathInputError("point cannot form an array") from exc
    if raw.shape != (2,):
        raise PathInputError("point must have shape (2,)")
    number_types = (int, float, np.integer, np.floating)
    for item in raw.flat:
        if isinstance(item, (bool, np.bool_)):
            raise PathInputError("Boolean is not a coordinate")
        if not isinstance(item, number_types):
            raise PathInputError("coordinate must be real")
    try:
        point = raw.astype(np.float64)
    except (TypeError, ValueError, OverflowError) as exc:
        raise PathInputError("coordinate cannot use float64") from exc
    if not np.all(np.isfinite(point)):
        raise PathInputError("coordinates must be finite")
    return point

def distance_array_example(start_xy, goal_xy) -> float:
    start = _point_array(start_xy)
    goal = _point_array(goal_xy)
    result = math.hypot(goal[0] - start[0], goal[1] - start[1])
    if not math.isfinite(result):
        raise PathInputError("distance must be finite")
    return result

def interpolate_example(start_xy, goal_xy, num_samples):
    start = _point_array(start_xy)
    goal = _point_array(goal_xy)
    if isinstance(num_samples, (bool, np.bool_)):
        raise PathInputError("sample count cannot be Boolean")
    if not isinstance(num_samples, (int, np.integer)):
        raise PathInputError("sample count must be an integer")
    if int(num_samples) < 2:
        raise PathInputError("sample count must be at least two")
    alpha = np.linspace(0.0, 1.0, int(num_samples))[:, None]
    points = start[None, :] + alpha * (goal - start)[None, :]
    points[0] = start
    points[-1] = goal
    if not np.all(np.isfinite(points)):
        raise PathInputError("interpolated points must be finite")
    return points

def path_loop_example(path):
    """Kernel for a validated, normalized float64 array (N, 2)."""
    total = 0.0
    for p0, p1 in zip(path[:-1], path[1:]):
        total += distance_array_example(p0, p1)
    if not math.isfinite(total):
        raise PathInputError("path length must be finite")
    return total

def path_array_example(path):
    """Kernel for a validated, normalized float64 array (N, 2)."""
    displacement = path[1:, :] - path[:-1, :]
    squared = displacement * displacement
    segment_lengths = np.sqrt(np.sum(squared, axis=1))
    result = float(np.sum(segment_lengths))
    if not np.isfinite(result):
        raise PathInputError("path length must be finite")
    return result

def batch_example(paths):
    """Kernel for a validated, normalized float64 array (B, N, 2)."""
    displacement = paths[:, 1:, :] - paths[:, :-1, :]
    segment_lengths = np.sqrt(np.sum(displacement**2, axis=2))
    lengths = np.sum(segment_lengths, axis=1)
    if not np.all(np.isfinite(lengths)):
        raise PathInputError("batch lengths must be finite")
    return lengths
