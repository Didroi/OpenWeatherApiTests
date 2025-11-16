import allure
import pytest

from tests.data.test_params import LANGUAGE_CITY_NAMES

'''import allure
import pytest
from allure_commons.types import Severity

@allure.epic("OpenWeather API")
@allure.feature("Geo.Feature")
@allure.story("Geo.Story")
@allure.suite("Geo Location Tests")
@allure.title("Get GEO location by city name")
@allure.description("Positive Functional read geo location by name")
@allure.severity(Severity.CRITICAL)  # BLOCKER, CRITICAL, NORMAL, MINOR, TRIVIAL
@allure.tag("API", "Smoke", "Regression", "Geo")
@allure.link("https://openweathermap.org/api/geocoding-api", name="API Documentation")
@pytest.mark.smoke
@pytest.mark.regression 

Иерархия организации тестов (от верхнего уровня к нижнему):

@allure.epic - самый высокий уровень (например, "API Testing")
@allure.feature - функциональность (у вас "Geo.Feature" - хорошо)
@allure.story - пользовательская история (у вас "Geo.Story" - хорошо)
@allure.suite - группа тестов (опционально)

2. Обязательные параметры для каждого теста:

@allure.title - понятное название ✅
@allure.description - описание ✅
@allure.severity - уровень критичности
@allure.tag - теги для фильтрации

3. Дополнительные элементы:

allure.step() - шаги теста для детализации выполнения
allure.attach() - прикрепление данных (request/response)
@allure.link - ссылки на документацию
@allure.issue / @allure.testcase - ссылки на баг-трекер/тест-кейсы
'''


@allure.epic("OpenWeather API Testing")
@allure.feature("Geocoding")
@allure.story("Direct geocoding by city name")
@allure.suite("Geocoding Tests")
@allure.title("Get coordinates by city name")
@allure.description(
    "Validate that direct geocoding API returns correct schema and successful "
    "response when searching coordinates by city name."
)
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_get_geo_by_city_name(get_geo):
    get_geo.get_geo_by_city_name("Praha")
    assert get_geo.check_status_is_(200)
    assert get_geo.has_response_valid_schema()


@allure.epic("OpenWeather API Testing")
@allure.feature("Geocoding")
@allure.story("Direct geocoding by ZIP code")
@allure.suite("Geocoding Tests")
@allure.title("Get coordinates by ZIP code")
@allure.description(
    "Ensure that ZIP code + country code based geocoding returns valid schema "
    "and a successful HTTP response."
)
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_get_geo_by_zip_code(get_geo):
    get_geo.get_geo_by_zip("454000", "RU")
    assert get_geo.check_status_is_(200)
    assert get_geo.has_response_valid_schema()


@allure.epic("OpenWeather API Testing")
@allure.feature("Geocoding")
@allure.story("Reverse geocoding with fixed coordinates")
@allure.suite("Geocoding Tests")
@allure.title("Get city name by hardcoded coordinates")
@allure.description(
    "Check that reverse geocoding returns a valid location name when using predefined latitude "
    "and longitude values."
)
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
def test_reverse_geo_lookup_hardcoded(get_geo):
    get_geo.reverse_geocoding_by_coordinates(50.0874654, 14.4212535)
    assert get_geo.check_status_is_(200)
    assert get_geo.has_response_valid_schema()


@allure.epic("OpenWeather API Testing")
@allure.feature("Geocoding")
@allure.story("Reverse geocoding using coordinates from fixture")
@allure.suite("Geocoding Tests")
@allure.title("Get city name by coordinates from ZIP fixture")
@allure.description(
    "Validate reverse geocoding when coordinates are obtained from another test fixture "
    "via ZIP lookup. Ensures data flow between two endpoints works correctly."
)
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_reverse_geo_lookup_from_fixture(get_geo, location_by_zip):
    get_geo.reverse_geocoding_by_coordinates(*location_by_zip)
    assert get_geo.check_status_is_(200)
    assert get_geo.has_response_valid_schema()


@allure.epic("OpenWeather API Testing")
@allure.feature("Weather")
@allure.story("Fetch weather data by coordinates")
@allure.suite("Weather Tests")
@allure.title("Get weather by coordinates from fixture")
@allure.description(
    "Validate that the Weather API correctly returns current weather data for coordinates "
    "obtained from ZIP-based geocoding."
)
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
def test_get_weather_by_coordinates_fixture(get_weather,
                                            location_by_zip):  # TODO: Использование не захардкоженного города в фикстуре
    get_weather.get_weather_by_coordinates(*location_by_zip)
    assert get_weather.check_status_is_(200)
    assert get_weather.has_response_valid_schema()


@allure.epic("OpenWeather API Testing")
@allure.feature("Weather")
@allure.story("Fetch weather data by city name")
@allure.suite("Weather Tests")
@allure.title("Get weather by city name")
@allure.description("Validate that the Weather API correctly returns current weather data for city name")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
def test_get_weather_by_city_name(get_weather):
    get_weather.get_weather_by_city_name("Paris")
    assert get_weather.check_status_is_(200)
    assert get_weather.has_response_valid_schema()


@allure.epic("OpenWeather API Testing")
@allure.feature("Weather")
@allure.story("Validate different measurement units")
@allure.suite("Weather Tests")
@allure.title("Get weather for different measurement units")
@allure.description(
    "Validate that the Weather API correctly returns current weather data for city in different measurement units")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.parametrize("units,temp_min,temp_max", [
    ("metric", -50, 50),
    ("imperial", -58, 122),
    ("standard", 223, 323),
])
def test_get_weather_with_different_units(get_weather, units, temp_min, temp_max):
    get_weather.get_weather_by_city_name('Prague', units=units)
    assert get_weather.check_status_is_(200)
    assert get_weather.has_response_valid_schema()
    assert get_weather.is_temperatura_in_correct_range(temp_min, temp_max)


@allure.epic("OpenWeather API Testing")
@allure.feature("Weather")
@allure.story("Validate different response type")
@allure.suite("Weather Tests")
@allure.title("Get weather for different modes of response type")
@allure.description(
    "Validate that the Weather API correctly returns current weather data for city in different response type")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.parametrize("mode", ["json", "xml", "html"])
def test_get_weather_api_response_in_different_modes(get_weather, mode):
    get_weather.get_weather_by_city_name('Prague', mode=mode)
    assert get_weather.check_status_is_(200)
    assert get_weather.is_response_in_headers_has_content_type(mode)
    assert get_weather.is_body_response_format(mode)


@allure.epic("OpenWeather API Testing")
@allure.feature("Weather")
@allure.story("Validate response in different language")
@allure.suite("Weather Tests")
@allure.title("Get weather for different measurement units")
@allure.description(
    "Validate that the Weather API correctly returns response in different language")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.parametrize("language, city_name", LANGUAGE_CITY_NAMES)
def test_get_weather_with_different_units(get_weather, language, city_name):
    get_weather.get_weather_by_city_name('Prague', lang=language)
    assert get_weather.check_status_is_(200)
    assert get_weather.has_response_valid_schema()
    assert get_weather.has_city_correct_name(city_name)
