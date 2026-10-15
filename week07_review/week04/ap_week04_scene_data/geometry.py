"""Supplied pure numerical functions reused from the Week 3 domain model."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def polyline_length(points: NDArray[np.float64]) -> float:
    """Return the Euclidean length of a two-dimensional waypoint array."""
    array = np.asarray(points, dtype=np.float64)
    if array.ndim != 2 or array.shape[0] < 2:
        raise ValueError("points must have shape (N, D) with N at least 2")
    return float(np.linalg.norm(np.diff(array, axis=0), axis=1).sum())

