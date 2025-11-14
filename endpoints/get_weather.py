import allure
import requests

from endpoints.base_api import BaseApi
from schemas.weather_schema import CurrentWeatherSchema


class GetWeather(BaseApi):
    WEATHER_URI = '/data/2.5/weather'

    @allure.step('Get weather - main simple try')
    def get_weather_by_geo_location(self, latitude, longitude):
        params = {
            'lat': f'{latitude}',
            'lon': f'{longitude}',
            'appid': self.api_key
        }

        self.response = requests.get(
            f'{self.base_url}{self.WEATHER_URI}',
            params=params
        )

        self.response_json = self.response.json()
        self.response_code = self.response.status_code
        self.current_schema = CurrentWeatherSchema
