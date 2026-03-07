import pytest

import src.api
from src.api import Parser, APIAdapter
from src.json_saver import JSONSaver

@pytest.fixture
def api_adapt():
    return APIAdapter()

def test_get_aeroplanes(api_adapt):
    assert src.api.APIAdapter.get_aeroplanes(api_adapt, "Canada") is None
