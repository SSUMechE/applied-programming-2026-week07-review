"""Small complete objects, not replacements for earlier Assignment APIs.

ReviewObstacle is a separate teaching type, not Week 4's frozen Obstacle API.
Names and centres in this example are already valid. Radius is the explicit
validation boundary: a finite, positive Python int or float, excluding Boolean.
Centres and radii use metres. The Point example accepts nonempty numeric tuples
or lists and illustrates ownership, not a complete coordinate validator.
"""

# BEGIN SNIPPET obstacle_imports
import math
# END SNIPPET obstacle_imports
from dataclasses import dataclass


# BEGIN SNIPPET inheritance
class RadiusError(ValueError):
    """An invalid radius is also an invalid value."""
# END SNIPPET inheritance


# BEGIN SNIPPET obstacle_class
class ReviewObstacle:
    def __init__(self, name, center, radius):
        self.name = name
        self.center = tuple(center)
        self.resize(radius)

    @property
    def radius(self):
        return self._radius

    def resize(self, new_radius):
        if (isinstance(new_radius, bool)
                or not isinstance(new_radius, (int, float))):
            raise RadiusError("radius must be a real number, not Boolean")
        try:
            value = float(new_radius)
        except OverflowError as error:
            raise RadiusError("radius must be finite and positive") from error
        if not math.isfinite(value) or value <= 0.0:
            raise RadiusError("radius must be finite and positive")
        self._radius = value
# END SNIPPET obstacle_class


# BEGIN SNIPPET frozen_point
@dataclass(frozen=True)
class Point:
    values: tuple

    def __post_init__(self):
        owned = tuple(self.values)
        if not owned:
            raise ValueError("values must not be empty")
        object.__setattr__(self, "values", owned)

    @property
    def count(self):
        return len(self.values)
# END SNIPPET frozen_point


# BEGIN SNIPPET scene_class
class Scene:
    def __init__(self, obstacles):
        self.obstacles = list(obstacles)
# END SNIPPET scene_class


def main():
    # BEGIN SNIPPET obstacle_calls
    first = ReviewObstacle("post", (0.0, 0.0), 0.5)
    second = ReviewObstacle("post", (0.0, 0.0), 0.5)
    alias = first
    alias.resize(0.75)
    print("same object:", alias is first)
    print("separate objects:", first is second)
    print("radii:", first.radius, second.radius)
    try:
        first.resize(0.0)
    except ValueError as error:
        print("rejected:", error)
    print("radius after rejection:", first.radius)
    # END SNIPPET obstacle_calls

    # BEGIN SNIPPET point_calls
    source = [2.0, 4.0]
    point = Point(source)
    source[0] = 99.0
    print("source:", source)
    print("stored:", point.values)
    print("count:", point.count)
    print("equal fields:", point == Point((2.0, 4.0)))
    # END SNIPPET point_calls

    # BEGIN SNIPPET composition
    scene = Scene([first, second])
    print("scene count:", len(scene.obstacles))
    print("first part is first:", scene.obstacles[0] is first)
    # END SNIPPET composition


if __name__ == "__main__":
    main()
