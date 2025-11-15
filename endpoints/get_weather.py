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
    def get_weather_by_city_name(self, city_name):
        params = {
            'q': city_name,
            'appid': self.api_key
        }

        self.response = requests.get(
            f'{self.base_url}{self.WEATHER_URI}',
            params=params
        )

        self.response_json = self.response.json()
        self.response_code = self.response.status_code
        self.current_schema = CurrentWeatherSchema
