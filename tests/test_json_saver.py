import pytest

import src.json_saver
from src.json_saver import JSONSaver


@pytest.fixture
def json_save():
    return JSONSaver()


def test_read_file(json_save):
    assert src.json_saver.JSONSaver.read_file(json_save) == [
        {
            "register_country": "United States",
            "call_name": "UAL1621",
            "flight_speed": 268.79,
            "flight_height": 10203.18,
            "is_on_ground": "False"
        },
        {
            "register_country": "Russia",
            "call_name": "UAL5040",
            "flight_speed": 235.19,
            "flight_height": 15234.06,
            "is_on_ground": "False"
        }
    ]
