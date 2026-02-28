import pytest

from src.func import state_list
from src.planes import Aeroplane


@pytest.fixture
def plane_1():
    return Aeroplane("United States", "UAL1621", 268.79, 10203.18, False)

def test_init_plane(plane_1):
    assert plane_1.register_country == "United States"
    assert plane_1.call_name == "UAL1621"
    assert plane_1.flight_speed == 268.79
    assert plane_1.flight_height == 10203.18
    assert plane_1.is_on_ground == False

def test_states(plane_1):
    assert state_list(plane_1) == ["United States", "UAL1621", 268.79, 10203.18, False]
