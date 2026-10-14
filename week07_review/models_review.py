"""Sampled geometric quantities and parameters, not robot motion or safety."""

import numpy as np


def main():
    # BEGIN SNIPPET model_sampling
    start = np.array([-2.0, 0.0])
    goal = np.array([2.0, 0.0])
    radius = 0.5
    for count in (2, 9):
        alpha = np.linspace(0.0, 1.0, count)[:, None]
        points = (1.0 - alpha) * start + alpha * goal
        distances = np.linalg.norm(points, axis=1)
        clearance = float(np.min(distances - radius))
        print(f"samples={count}: sampled clearance={clearance:.1f} m")
    # END SNIPPET model_sampling

    # BEGIN SNIPPET model_margin
    measured_clearance = 1.5
    for required_clearance in (0.5, 1.5, 1.6):
        margin = measured_clearance - required_clearance
        print(f"required={required_clearance:.1f}: "
              f"margin={margin:.1f}, accepted={margin >= 0.0}")
    # END SNIPPET model_margin

    # BEGIN SNIPPET grid_pairs
    xs = np.linspace(-1.0, 1.0, 3)
    ys = np.linspace(-1.0, 1.0, 3)
    pairs = [(float(x), float(y)) for x in xs for y in ys]
    print("x values:", xs)
    print("y values:", ys)
    print("grid count:", len(pairs))
    print("first / last:", pairs[0], pairs[-1])
    # END SNIPPET grid_pairs


if __name__ == "__main__":
    main()
