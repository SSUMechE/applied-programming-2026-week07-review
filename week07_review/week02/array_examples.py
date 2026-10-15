# Fresh Python session
import numpy as np
path = np.asarray(
    [(0.0, 0.0), (3.0, 0.0), (3.0, 4.0)],
    dtype=np.float64,
)

print(path.ndim)
print(path.shape)
print(path[1, 0])

path = np.array([[0.0, 0.0], [3.0, 0.0], [3.0, 4.0]])
middle_view = path[1:2]
middle_view[0, 0] = 99.0
print(path)

from learning_geometry import distance_array_example

candidate = np.array([[0.0, 0.0], [3.0, 4.0]])
snapshot = candidate.copy()
result = distance_array_example(candidate[0], candidate[1])
assert np.isclose(result, 5.0, rtol=1e-12, atol=1e-12)
assert np.array_equal(candidate, snapshot)
print(result)

# Continue with numpy imported; this is the numerical kernel.
start = np.asarray((0.0, 0.0), dtype=np.float64)  # (2,)
goal = np.asarray((3.0, 4.0), dtype=np.float64)   # (2,)
alpha = np.linspace(0.0, 1.0, 5)[:, None]        # (5, 1)

points = start[None, :] + alpha * (goal - start)[None, :]
points[0] = start
points[-1] = goal
print(points.shape)
print(points)

import numpy as np

from learning_geometry import interpolate_example

start = np.array([1.0, 1.0])
goal = np.array([0.1, 0.1])
points = interpolate_example(start, goal, 3)
assert points.shape == (3, 2)
assert np.array_equal(points[0], start)
assert np.array_equal(points[-1], goal)
print(points)

import numpy as np
from learning_geometry import distance_array_example, path_loop_example

path = np.array([[0.0, 0.0], [3.0, 0.0], [3.0, 4.0]])
print(distance_array_example(path[0], path[-1]))
print(path_loop_example(path))

import numpy as np
from learning_geometry import path_array_example, path_loop_example

path = np.array([[0.0, 0.0], [3.0, 0.0], [3.0, 4.0]])
actual = path_array_example(path)
expected = path_loop_example(path)
assert np.isclose(actual, expected, rtol=1e-12, atol=1e-12)
assert np.isclose(actual, 7.0, rtol=1e-12, atol=1e-12)
print(actual)

import numpy as np
from learning_geometry import batch_example

paths = np.array([
    [[0.0, 0.0], [3.0, 0.0], [3.0, 4.0]],
    [[1.0, 1.0], [7.0, 1.0], [7.0, 5.0]],
], dtype=np.float64)
print(paths.shape)
lengths = batch_example(paths)
print(lengths.shape)
print(lengths)

from learning_geometry import batch_example, path_loop_example

actual = batch_example(paths)
scalar = np.array([path_loop_example(row) for row in paths])
assert actual.shape == (2,)
assert np.allclose(actual, [7.0, 10.0], rtol=1e-12, atol=1e-12)
assert np.allclose(actual, scalar, rtol=1e-12, atol=1e-12)

shift = np.array([10.0, -2.0])
translated = batch_example(paths + shift)
assert np.allclose(translated, actual, rtol=1e-12, atol=1e-12)

snapshot = paths.copy()
_ = batch_example(paths)
assert np.array_equal(paths, snapshot)
permuted = batch_example(paths[::-1])
assert np.allclose(permuted, actual[::-1], rtol=1e-12, atol=1e-12)
print("All four consistency checks passed")
