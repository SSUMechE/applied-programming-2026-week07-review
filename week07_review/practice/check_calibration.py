"""Supplied checks. Run with the explicit filename shown in the Reading."""
import pytest
from calibration import LinearCalibration, MeasurementSet


@pytest.mark.parametrize("gain,offset,raw,expected", [
    (2.0, 1.0, 3.0, 7.0),
    (0.5, -2.0, 8.0, 2.0),
])
def test_calibration_case(gain, offset, raw, expected):
    calibration = LinearCalibration(gain, offset)
    assert LinearCalibration.output_unit == "mm"
    assert calibration.gain == gain
    assert calibration.offset_mm == offset
    assert calibration.apply(raw) == pytest.approx(expected, rel=1e-12, abs=1e-12)


@pytest.mark.parametrize("readings,gain,offset,expected", [
    ([1.0, 3.0], 2.0, 1.0, [3.0, 7.0]),
    ([4.0, 8.0], 0.5, -2.0, [0.0, 2.0]),
])
def test_measurement_values(readings, gain, offset, expected):
    calibration = LinearCalibration(gain, offset)
    measurements = MeasurementSet(readings, calibration)
    assert measurements.calibration is calibration
    assert isinstance(measurements.raw, tuple)
    assert measurements.raw == tuple(readings)
    result = measurements.corrected()
    assert isinstance(result, list)
    assert result == pytest.approx(expected, rel=1e-12, abs=1e-12)


def test_measurement_ownership():
    source = [1.0, 3.0]
    calibration = LinearCalibration(2.0, 1.0)
    measurements = MeasurementSet(source, calibration)
    source[0] = 99.0
    result = measurements.corrected()
    result[0] = 99.0
    assert measurements.raw == (1.0, 3.0)
    assert measurements.corrected() == [3.0, 7.0]


def test_measurement_calls_current_calibration():
    calibration = LinearCalibration(2.0, 1.0)
    measurements = MeasurementSet([1.0, 3.0], calibration)
    calibration.offset_mm = -1.0
    assert measurements.corrected() == [1.0, 5.0]
