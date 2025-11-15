import pytest

from endpoints.get_geo import GetGeo
from endpoints.get_weather import GetWeather


@pytest.fixture()
def location_by_zip():
    create_object = GetGeo()
    create_object.get_geo_by_zip("454000", "RU")
    lat = create_object.response_json["lat"]
    lon = create_object.response_json["lon"]
    yield lat, lon


@pytest.fixture()
def get_geo():
    return GetGeo()


@pytest.fixture()
def get_weather():
    return GetWeather()
