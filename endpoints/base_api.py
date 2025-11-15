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

    @allure.step("Validate HTTP status code is {code}")
    def check_status_is_(self, code):
        return self.response.status_code == code

    @allure.step("Validate response matches expected schema")
    def has_response_valid_schema(self):
        response_data = self.response_json

        if isinstance(response_data, list):
            if len(response_data) == 0:
                raise AssertionError("Response is empty list")
            response_data = response_data[0]

        validated = self.current_schema(**response_data)
        return True
