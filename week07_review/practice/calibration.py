"""Two short OOP review exercises. All supplied inputs are valid."""

# BEGIN E1_CLASS
class LinearCalibration:
    # Add output_unit and complete the initializer in this region.
    def __init__(self, gain, offset_mm):
        raise NotImplementedError("Complete E1_CLASS")
# END E1_CLASS

    def apply(self, raw):
        # BEGIN E1_APPLY
        raise NotImplementedError("Complete E1_APPLY")
        # END E1_APPLY
        return corrected_mm


class MeasurementSet:
    def __init__(self, readings, calibration):
        # BEGIN E2_INIT
        raise NotImplementedError("Complete E2_INIT")
        # END E2_INIT

    def corrected(self):
        # BEGIN E2_VALUES
        raise NotImplementedError("Complete E2_VALUES")
        # END E2_VALUES
        return values_mm


def show_calibrations():
    for gain, offset, raw in ((2.0, 1.0, 3.0), (0.5, -2.0, 8.0)):
        calibration = LinearCalibration(gain, offset)
        print("unit:", calibration.output_unit)
        print("corrected:", calibration.apply(raw))


def show_measurements():
    for readings, gain, offset in (([1.0, 3.0], 2.0, 1.0),
                                  ([4.0, 8.0], 0.5, -2.0)):
        calibration = LinearCalibration(gain, offset)
        measurements = MeasurementSet(readings, calibration)
        print("same calibration:", measurements.calibration is calibration)
        print("stored raw:", measurements.raw)
        print("corrected:", measurements.corrected())


if __name__ == "__main__":
    import sys

    if sys.argv[1:] == ["1"]:
        show_calibrations()
    elif sys.argv[1:] == ["2"]:
        show_measurements()
    else:
        print("Use: python calibration.py 1   or   python calibration.py 2")
