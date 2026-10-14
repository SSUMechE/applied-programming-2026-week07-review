"""Complete worked examples for function calls, returned values and containers."""

import math
import numpy as np


# BEGIN SNIPPET functions_definition
def mm_to_m(value_mm):
    """Convert a finite, nonnegative Python int or float from mm to m."""
    if isinstance(value_mm, bool) or not isinstance(value_mm, (int, float)):
        raise ValueError("length must be a real number, not Boolean")
    try:
        value = float(value_mm)
    except OverflowError as error:
        raise ValueError("length must be finite") from error
    if not math.isfinite(value) or value < 0.0:
        raise ValueError("length must be finite and nonnegative")
    return value / 1000.0
# END SNIPPET functions_definition


def main():
    # BEGIN SNIPPET functions_calls
    length_m = mm_to_m(12.5)
    print("returned length:", length_m)
    print("zero length:", mm_to_m(0.0))
    try:
        mm_to_m(-1.0)
    except ValueError as error:
        print("rejected:", error)
    # END SNIPPET functions_calls

    # BEGIN SNIPPET functions_containers
    start = (2.0, 4.0)
    x, y = start
    readings_mm = [0.0, 12.5]
    readings_mm.append(25.0)
    converted = []
    for value in readings_mm:
        converted.append(mm_to_m(value))
    compact = [mm_to_m(value) for value in readings_mm]
    print("unpacked:", x, y)
    print("first two:", readings_mm[:2])
    print("converted:", converted)
    print("same values:", converted == compact)
    # END SNIPPET functions_containers

    # BEGIN SNIPPET tolerance_calls
    print(np.isclose(100.05, 100.0, rtol=0.001, atol=1e-6))
    print(np.isclose(0.0001, 0.0, rtol=0.001, atol=1e-6))
    # END SNIPPET tolerance_calls


if __name__ == "__main__":
    main()
