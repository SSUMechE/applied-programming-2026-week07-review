"""Independent chapter practice, not the Assignment 3 Configuration solution.

Run this file separately from 01_instances.py. This is a new class definition.
Its simplified contract only converts input to a tuple and rejects an empty
tuple. It does not validate numerical types, finiteness, or array shape.
"""

from dataclasses import FrozenInstanceError, dataclass


@dataclass(frozen=True)
class Configuration:
    values: tuple

    def __post_init__(self):
        owned = tuple(self.values)
        if not owned:
            raise ValueError("values must not be empty")
        object.__setattr__(self, "values", owned)

    @property
    def dimension(self):
        return len(self.values)


def main():
    source = [0.0, 0.0]
    q = Configuration(source)
    source[0] = 99.0

    print("caller list:", source)
    print("stored tuple:", q.values)
    print("q.dimension:", q.dimension)
    print("equal values:", q == Configuration((0.0, 0.0)))

    try:
        Configuration(())
    except ValueError as error:
        print("empty input rejected:", error)

    try:
        q.values = (9.0, 9.0)
    except FrozenInstanceError:
        print("field reassignment rejected: FrozenInstanceError")


if __name__ == "__main__":
    main()
