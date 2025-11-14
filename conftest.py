import pytest

from endpoints.get_geo import GetGeo


@pytest.fixture()
def location_by_zip():
    print('Start testing')
    create_object = GetGeo()
    create_object.get_geo_by_zip_code("454000", "RU")
    lat = create_object.response_json["lat"]
    lon = create_object.response_json["lon"]
    print(lat)
    print(lon)
    yield lat, lon
    print('Testing completed')


@pytest.fixture()
def follow_the_testing_without_object():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def get_geo():
    return GetGeo()
