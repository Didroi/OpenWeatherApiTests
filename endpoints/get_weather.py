import json
import xml.etree.ElementTree as ElT

import allure
import requests

from endpoints.base_api import BaseApi
from schemas.weather_schema import CurrentWeatherSchema


class GetWeather(BaseApi):
    WEATHER_URI = '/data/2.5/weather'

    @allure.step("Send GET /data/2.5/weather with coordinates lat: {latitude}, lon: {longitude}")
    def get_weather_by_coordinates(self, latitude, longitude):
        params = {
            'lat': latitude,
            'lon': longitude,
            'appid': self.api_key
        }

        self.response = requests.get(
            f'{self.base_url}{self.WEATHER_URI}',
            params=params
        )

        self.response_json = self.response.json()
        self.response_code = self.response.status_code
        self.current_schema = CurrentWeatherSchema

    @allure.step("Send GET /data/2.5/weather with city name: {city_name}")
    def get_weather_by_city_name(self, city_name, units=None, mode=None, lang=None):
        params = {
            'q': city_name,
            'appid': self.api_key
        }
        if units:
            params['units'] = units
        if mode:
            params['mode'] = mode
        if lang:
            params['lang'] = lang

        self.response = requests.get(
            f'{self.base_url}{self.WEATHER_URI}',
            params=params
        )

        if not mode or mode == "json":
            self.response_json = self.response.json()
        self.response_code = self.response.status_code
        self.current_schema = CurrentWeatherSchema
        self.content_type = self.response.headers.get('Content-Type')

    @allure.step("Check temperature is in correct range [{min_temp}, {max_temp}]")
    def is_temperatura_in_correct_range(self, min_temp, max_temp):
        actual_temp = self.response_json['main']['temp']
        return min_temp <= actual_temp <= max_temp

    @allure.step("Check response payload format is {expected_format}")
    def is_body_response_format(self, expected_format):
        text = self.response.text.strip()

        if expected_format == 'json':
            try:
                json.loads(text)
                return True
            except (json.JSONDecodeError, ValueError):
                return False
        elif expected_format == 'xml':
            try:
                ElT.fromstring(text)
                return True
            except ElT.ParseError:
                return False
        elif expected_format == 'html':
            return '<html' in text.lower() or '<!doctype' in text.lower()
        else:
            raise ValueError(
                f"Unsupported format: '{expected_format}'. "
                f"Expected one of: 'json', 'xml', 'html'"
            )

    @allure.step("Check is the city name {city_name} correct in different languages")
    def has_city_correct_name(self, city_name):
        return self.response_json['name'] == city_name
