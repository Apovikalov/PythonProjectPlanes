import pytest

from src.func import (state_list, filter_aeroplanes, get_aeroplanes_by_altitude,
                      sort_aeroplanes, get_top_aeroplanes)
from src.planes import Aeroplane


@pytest.fixture
def plane_1():
    return Aeroplane("United States", "UAL1621", 268.79, 10203.18, False)

@pytest.fixture
def plane_2():
    return Aeroplane("Russia", "UAL5040", 235.19, 15234.06, False)

@pytest.fixture
def plane_3():
    return Aeroplane("Russia", "UAL2276", 207.19, 8567.19, False)

@pytest.fixture
def plane_4():
    return Aeroplane("Oman", "UAL3319", 242.81, 13217.77, False)

def test_init_plane(plane_1):
    assert plane_1.register_country == "United States"
    assert plane_1.call_name == "UAL1621"
    assert plane_1.flight_speed == 268.79
    assert plane_1.flight_height == 10203.18
    assert plane_1.is_on_ground == False

def test_states(plane_1):
    assert state_list(plane_1) == ["United States", "UAL1621", 268.79, 10203.18, False]

def test_filter(plane_1, plane_2, plane_3, plane_4):
    assert filter_aeroplanes([plane_1, plane_2, plane_3, plane_4], "Russia Oman") == [plane_2, plane_3, plane_4]

def test_altitude(plane_1, plane_2, plane_3, plane_4):
    assert get_aeroplanes_by_altitude([plane_1, plane_2, plane_3, plane_4], 10000, 15000) == [plane_1, plane_4]