import allure
import requests
from config import API_KEY, BASE_URL


class BaseApi:
    response: requests.Response
    response_json: dict
    response_code: int
    current_schema = None

    def __init__(self):
        self.api_key: str = API_KEY
        self.base_url: str = BASE_URL

    @allure.step('Check status code')
    def check_status_is_(self, code):
        return self.response.status_code == code

    @allure.step('Check response Name')
    def check_response_name_is_(self, name):
        return self.response_json['name'] == name

    @allure.step('Check response schema')
    def has_response_valid_schema(self):
        response_data = self.response_json

        if isinstance(response_data, list):
            if len(response_data) == 0:
                raise AssertionError("Response is empty list")
            response_data = response_data[0]

        validated = self.current_schema(**response_data)
        return True
