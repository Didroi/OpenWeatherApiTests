# OpenWeather API Test Automation

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Pytest](https://img.shields.io/badge/pytest-9.0.0-green)
![Allure Report](https://img.shields.io/badge/allure--pytest-2.15.0-orange)
![Requests](https://img.shields.io/badge/requests-2.32.5-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

API test automation framework for [OpenWeather API](https://openweathermap.org/api) using Python, Pytest, and Allure Report.

> 💡 **Note:** After setting up CI/CD, add this badge at the top: `![Tests](https://github.com/Didroi/openweather-api-tests/workflows/API%20Tests/badge.svg)`

## 📋 About

This project demonstrates automated API testing skills with clean architecture, comprehensive test coverage, and detailed reporting. Built following industry best practices and design patterns.

**Architecture:** Uses Endpoint Object Pattern (API equivalent of Page Object Pattern) where each API endpoint is represented as a separate class with methods containing `@allure.step` decorators for detailed test reporting.

## 🛠 Tech Stack

- **Python 3.10+** - Programming language (tested on Python 3.12)
- **Pytest** - Testing framework
- **Requests** - HTTP library
- **Allure Report** - Test reporting
- **python-dotenv** - Environment management

## 📂 Project Structure

```
OpenWeather/
├── endpoints/              # API endpoint classes (Endpoint Object Pattern)
│   ├── base_api.py        # Base API class with common methods
│   ├── get_geo.py         # Geo API endpoints (with @allure.step)
│   └── ...                # Other API endpoints
├── tests/                 # Test suite
│   ├── data/              # Test data (payloads, schemas)
│   │   ├── headers.py
│   │   ├── params.py
│   │   └── payloads.py
│   ├── test_api.py        # API tests
│   └── conftest.py        # Pytest fixtures
├── allure-results/        # Allure test results
├── config.py              # Configuration
├── .env                   # Environment variables (not in repo)
├── .gitignore
└── requirements.txt       # Dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- OpenWeather API key ([Get free key](https://home.openweathermap.org/api_keys))

### Installation

1. Clone the repository
```bash
git clone https://github.com/Didroi/openweather-api-tests.git
cd openweather-api-tests
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure environment variables

Create `.env` file in project root:
```env
API_KEY=your_openweather_api_key
BASE_URL=https://api.openweathermap.org
```

### Running Tests

Execute all tests:
```bash
pytest tests/
```

Run with Allure results:
```bash
pytest tests/ --alluredir=allure-results
```

Run specific test markers:
```bash
pytest tests/ -m smoke
pytest tests/ -m regression
```

### Generate Allure Report

```bash
allure serve allure-results
```

## 🧪 Test Coverage

### Implemented Endpoints

| Endpoint | Method | Status |
|----------|--------|--------|
| `/geo/1.0/direct` | GET | ✅ Completed |
| More endpoints | - | 🚧 In Progress |

### Test Scenarios

**Positive Tests:**
- ✅ Get geo location by city name
- ✅ Verify response structure
- ✅ Validate status codes

**Negative Tests:**
- 🚧 Invalid city name
- 🚧 Missing API key
- 🚧 Empty parameters

**Parametrized Tests:**
- 🚧 Multiple cities
- 🚧 Boundary values

## 📊 Test Example

> **Note:** Allure steps (`@allure.step`) are implemented inside endpoint methods (e.g., `get_geo.py`), keeping test code clean and focused.

**Test code:**
```python
@allure.epic('OpenWeather API testing')
@allure.feature('Geo')
@allure.story('Geo by location name')
@allure.title('Get GEO by location name')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
def test_read_geo_by_location_name(follow_the_testing_without_object, get_geo):
    get_geo.get_geo_by_location_name("Prague")
    
    assert get_geo.check_status_is_(200)
    assert get_geo.response_json is not None
```

**Endpoint method with Allure steps:**
```python
class GetGeo(BaseApi):
    GEO_URI = '/geo/1.0/direct'
    
    @allure.step('Get GEO by location name')
    def get_geo_by_location_name(self, geo_name, limit=5):
        params = {
            'q': geo_name,
            'limit': limit,
            'appid': self.api_key
        }
        self.response = requests.get(
            url=f'{self.base_url}{self.GEO_URI}',
            params=params
        )
        self.response_json = self.response.json()
        self.response_code = self.response.status_code
```

## 🎯 Features

- ✅ Endpoint Object Pattern (API equivalent of Page Object)
- ✅ Pytest fixtures for test setup
- ✅ Allure reporting with detailed steps
- ✅ Environment configuration management
- ✅ Test data separation
- 🚧 JSON schema validation
- 🚧 Parametrized tests
- 🚧 CI/CD pipeline (GitHub Actions)
- 🚧 Logging

## 📝 Roadmap

- [ ] Add more endpoint coverage
- [ ] Implement negative test scenarios
- [ ] Add JSON schema validation
- [ ] Set up CI/CD with GitHub Actions
- [ ] Add logging functionality
- [ ] Increase parametrization

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Dmitrii Kiselev**
- GitHub: [@Didroi](https://github.com/Didroi)
- LinkedIn: [dmitrii-kiselev](https://linkedin.com/in/dmitrii-kiselev)

---

⭐ Star this repository if you find it helpful!