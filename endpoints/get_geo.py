import requests
import allure
from endpoints.base_api import BaseApi
from schemas.geo_schema import GeoByLocationOrCoordinatesSchema, GeoByZipCodeSchema


class GetGeo(BaseApi):
    GEO_URI = '/geo/1.0/'

    @allure.step('Get GEO by location name')
    def get_geo_by_location_name(self, geo_name, limit = 5):
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


    @allure.step('Get GEO by ZIP code')
    def get_geo_by_zip_code(self, zip_code, country_code):
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

    @allure.step('Get location name by coordinates')
    def get_location_name_by_geo(self, lat, lon, limit = 5):
        params = {
            'lat': f'{lat}',
            'lon': f'{lon}',
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
