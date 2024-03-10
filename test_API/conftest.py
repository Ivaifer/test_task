import pytest
import requests

from .configuration import URL_NEAREST_STATION, PARAMS_PENZA


@pytest.fixture
def third_station_code():
    response = requests.get(URL_NEAREST_STATION, params=PARAMS_PENZA)
    data = response.json()
    third_station = data['stations'][2]['code']
    return third_station
