"""Complete NumPy traces. Rows are inspection points, coordinates are in mm."""

import numpy as np


def main():
    # BEGIN SNIPPET arrays_basic
    points = np.array([[2., 4.], [6., 8.], [10., 12.]])
    print("shape:", points.shape)
    print("second x:", points[1, 0])
    print("row / one-row slice:", points[1].shape, points[1:2].shape)
    # END SNIPPET arrays_basic

    # BEGIN SNIPPET arrays_axis
    print("sum each row:", np.sum(points, axis=1))
    print("sum each coordinate:", np.sum(points, axis=0))
    # END SNIPPET arrays_axis

    # BEGIN SNIPPET arrays_broadcast
    shift = np.array([1., -2.])
    translated = points + shift
    print("translated:")
    print(translated)
    # END SNIPPET arrays_broadcast

    # BEGIN SNIPPET arrays_copy
    shared_source = points.copy()
    view = shared_source[1:2]
    view[0, 0] = 99.0
    independent_source = points.copy()
    copied = independent_source[1:2].copy()
    copied[0, 0] = 99.0
    print("after view edit:", shared_source[1])
    print("after copy edit:", independent_source[1])
    # END SNIPPET arrays_copy

    # BEGIN SNIPPET arrays_batch
    batch = np.array([points, translated])
    print("batch shape:", batch.shape)
    print("first point from each set:")
    print(batch[:, 0, :])
    totals = np.sum(batch, axis=1)
    print("total shape:", totals.shape)
    print(totals)
    # END SNIPPET arrays_batch

    # BEGIN SNIPPET arrays_interpolate
    start, end = points[0], points[-1]
    alpha = np.linspace(0.0, 1.0, 3)[:, None]
    samples = (1.0 - alpha) * start + alpha * end
    samples[0], samples[-1] = start, end
    print("three samples including endpoints:")
    print(samples)
    # END SNIPPET arrays_interpolate


if __name__ == "__main__":
    main()
