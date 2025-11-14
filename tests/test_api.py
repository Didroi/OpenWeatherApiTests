import allure
import pytest

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


@allure.epic('OpenWeather API testing')
@allure.feature('Geo')
@allure.story('Geo by location name')
@allure.suite("Geo Location Tests")
@allure.title('Get Geo by location name')
@allure.description('Positive Functional reading of geo location by name')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
def test_read_geo_by_location_name(get_geo):
    get_geo.get_geo_by_location_name("Praha")
    assert get_geo.check_status_is_(200)
    assert get_geo.has_response_valid_schema()


@allure.epic('OpenWeather API testing')
@allure.feature('Geo')
@allure.story('Geo by ZIP code and country code')
@allure.suite("Geo Location Tests")
@allure.title('Get Geo by location name')
@allure.description('Positive Functional reading of geo location by ZIP code')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
def test_read_geo_by_zip_code(get_geo):
    get_geo.get_geo_by_zip_code("454000", "RU")
    assert get_geo.check_status_is_(200)
    assert get_geo.has_response_valid_schema()


@allure.epic('OpenWeather API testing')
@allure.feature('Geo')
@allure.story('City name by hardcode Geo location')
@allure.suite("Geo Location Tests")
@allure.title('Get name by hardcode Geo location')
@allure.description('Positive Functional reading name of city by geo')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
def test_read_name_by_hc_geo(get_geo):
    get_geo.get_location_name_by_geo(50.0874654, 14.4212535)
    assert get_geo.check_status_is_(200)
    assert get_geo.has_response_valid_schema()


@allure.epic('OpenWeather API testing')
@allure.feature('Weather')
@allure.story('Weather by Geo location')
@allure.suite("OpenWeather Tests")
@allure.title('Get Weather by Geo location')
@allure.description('Positive Functional reading name of city by geo by using location from script')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_read_name_by_fixture_geo(get_geo, location_by_zip):
    get_geo.get_location_name_by_geo(*location_by_zip)
    assert get_geo.check_status_is_(200)
    assert get_geo.has_response_valid_schema()


@allure.epic('OpenWeather API testing')
@allure.feature('Geo')
@allure.story('City name by fixture Geo location')
@allure.suite("Geo Location Tests")
@allure.title('Get name by fixture Geo location')
@allure.description('Positive Functional response weather by geo')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
def test_get_weather_by_geo_location(get_weather,
                                     location_by_zip):  # TODO: Использование не захардкоженного города в фикстуре
    get_weather.get_weather_by_geo_location(*location_by_zip)
    assert get_weather.check_status_is_(200)
    assert get_weather.has_response_valid_schema()
