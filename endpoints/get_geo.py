import allure
import requests

from endpoints.base_api import BaseApi
from schemas.geo_schema import GeoByLocationOrCoordinatesSchema, GeoByZipCodeSchema


class GetGeo(BaseApi):
    GEO_URI = '/geo/1.0/'

    @allure.step("Send GET /geo/1.0/direct with city name: '{geo_name}' and limit: {limit}")
    def get_geo_by_city_name(self, geo_name, limit=5):
        params = {
            'q': geo_name,
            'limit': limit,
            'appid': self.api_key
        }

        self.response = requests.get(
            f'{self.base_url}{self.GEO_URI}direct',
            params=params
        )

        self.response_json = self.response.json()
        self.response_code = self.response.status_code
        self.current_schema = GeoByLocationOrCoordinatesSchema

    @allure.step("Send GET /geo/1.0/zip with ZIP: '{zip_code}', country: '{country_code}'")
    def get_geo_by_zip(self, zip_code, country_code):
        params = {
            'zip': f'{zip_code},{country_code}',
            'appid': self.api_key
        }

        self.response = requests.get(
            f'{self.base_url}{self.GEO_URI}zip',
            params=params
        )

        self.response_json = self.response.json()
        self.response_code = self.response.status_code
        self.current_schema = GeoByZipCodeSchema

    @allure.step("Send GET /geo/1.0/reverse with lat: {latitude}, lon: {longitude}, limit: {limit}")
    def reverse_geocoding_by_coordinates(self, latitude, longitude, limit=5):
        params = {
            'lat': latitude,
            'lon': longitude,
            'limit': limit,
            'appid': self.api_key
        }

        self.response = requests.get(
            f'{self.base_url}{self.GEO_URI}reverse',
            params=params
        )

        self.response_json = self.response.json()
        self.response_code = self.response.status_code
        self.current_schema = GeoByLocationOrCoordinatesSchema
