import pytest

from working import convert

def test_12_hour_formats():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_midnight_and_noon():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("11:59 PM to 12:00 AM") == "23:59 to 00:00"


def test_raises_value_error():
    invalid_inputs = [
        "9:00 to 5:00",
        "9 AM - 5 PM",
        "13:00 PM to 5:00 PM",
        "12:60 AM to 1:00 PM",
        "0 AM to 5 PM",
        "9:00 AM to 5:60 PM",
        "9:00AM to 5:00 PM",
        "9 AM to 5PM",
    ]

    for invalid in invalid_inputs:
        with pytest.raises(ValueError):
            convert(invalid)
