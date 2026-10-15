import numpy as np

actual = np.array([5.000004, 5.000020])
print(np.isclose(actual, 5.0, rtol=1e-6, atol=1e-8))

near_zero = np.array([5e-10, 5e-8])
print(np.isclose(near_zero, 0.0, rtol=1e-6, atol=1e-9))

expected = np.array([7.0, 10.0])
actual = np.array([7.0 + 1e-13, 10.0])
assert actual.shape == expected.shape
print(np.allclose(actual, expected, rtol=1e-12, atol=1e-12))
# True: every element passes the numerical comparison
