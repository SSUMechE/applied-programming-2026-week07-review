"""Exercise 2: replace the indicated region with your own checks."""
from calibration import LinearCalibration, MeasurementSet


def test_connection_and_ownership():
    calibration = LinearCalibration(2.0, 1.0)
    source = [1.0, 3.0]
    measurements = MeasurementSet(source, calibration)
    source[0] = 99.0
    result = measurements.corrected()
    # BEGIN E2_ASSERT
    raise NotImplementedError("Complete E2_ASSERT with assert checks")
    # END E2_ASSERT
