# OpenWeather API Test Automation

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Pytest](https://img.shields.io/badge/pytest-9.0.0-green)
![Allure Report](https://img.shields.io/badge/allure--pytest-2.15.0-orange)
![Requests](https://img.shields.io/badge/requests-2.32.5-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

API test automation framework for  [**OpenWeather API**](https://openweathermap.org/api) built with Python, Pytest, and
Allure.  
Project demonstrates real-world API testing skills using clean architecture, Allure annotations, fixtures, schema
validation, and chained endpoint logic.

> 💡 **CI/CD badge** can be added later when GitHub Actions pipeline becomes available.

---

## 📋 About

This project implements API automation using a clean, scalable structure following the **Endpoint Object Pattern**  
(API equivalent of Page Object Pattern).  
Each endpoint is represented by a separate class containing request logic, validation helpers, and Allure steps.

All tests are fully annotated using Allure:

- `@allure.epic`
- `@allure.feature`
- `@allure.story`
- `@allure.suite`
- `@allure.title`
- `@allure.description`
- `@allure.severity`

Fixtures provide data flow between endpoints (e.g., ZIP → GEO → WEATHER).

Schema validation is applied to every endpoint.

---

## 🛠 Tech Stack

- **Python 3.10+**
- **Pytest 9**
- **Requests**
- **Allure Report**
- **python-dotenv** — environment variables
- **JSON Schema** — response structure validation

---

## 📂 Project Structure

```
OpenWeather/
├── endpoints/
│   ├── base_api.py               # Common API logic
│   ├── get_geo.py                # Direct, ZIP-based, and reverse geocoding endpoints
│   ├── get_weather.py            # Current weather endpoint
│   └── ...
│
├── tests/
│   ├── data/
│   │   ├── schemas/              # JSON Schemas for API validation
│   │   ├── headers.py
│   │   ├── params.py
│   │   └── payloads.py
│   ├── conftest.py               # Fixtures (API clients, ZIP lookup fixture, env setup)
│   ├── test_api.py               # Main API test suite (with full Allure annotations)
│   └── ...
│
├── config.py                     # Base URL, env config
├── .env                          # API key & config (ignored by Git)
├── .gitignore
├── requirements.txt
└── allure-results/
```

---

## 🚀 Getting Started

### 1. Clone repository

```bash
git clone https://github.com/Didroi/openweather-api-tests.git
cd openweather-api-tests
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment

Create `.env`:

```env
API_KEY=your_openweather_api_key
BASE_URL=https://api.openweathermap.org
```

---

## ▶ Running Tests

Run all tests:

```bash
pytest tests/
```

With Allure:

```bash
pytest tests/ --alluredir=allure-results
```

Open report:

```bash
allure serve allure-results
```

Run specific markers:

```bash
pytest -m smoke
pytest -m regression
```

---

## 🧪 Test Coverage

### ✔ Implemented Endpoints

| Endpoint            | Method | Status                   |
|---------------------|--------|--------------------------|
| `/geo/1.0/direct`   | GET    | ✅ Direct geocoding       |
| `/geo/1.0/zip`      | GET    | ✅ ZIP → GEO              |
| `/geo/1.0/reverse`  | GET    | ✅ Reverse geocoding      |
| `/data/2.5/weather` | GET    | ✅ Weather by coordinates |

---

## ✔ Test Scenarios

### **Positive tests**

- Get coordinates by city name
- Get coordinates by ZIP code
- Reverse geocoding (hardcoded coords)
- Reverse geocoding (coords from ZIP)
- Weather by coordinates (from ZIP lookup)
- Cross-endpoint chain: **ZIP → GEO → WEATHER**
- Response schema validation
- Status code validation

### **Negative tests (planned)**

- Invalid city name
- Empty parameters
- Missing API key
- Invalid ZIP
- Boundary values

### **Parametrization**

🚧 Planned (lists of cities, ZIP codes, etc.)

---

## 📊 Test Example (REAL **current** structure)

Below is an example exactly matching the style of your current test suite.

```python
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
```

---

## 📡 Example Endpoint (with Allure steps)

```python
class GetGeo(BaseApi):

    @allure.step("Get GEO by city name: {city_name}")
    def get_geo_by_city_name(self, city_name, limit=5):
        params = {"q": city_name, "limit": limit, "appid": self.api_key}
        self._send_request("/geo/1.0/direct", params)
        return self
```

---

## 🎯 Features

- ✔ Endpoint Object Pattern
- ✔ Allure step annotations
- ✔ Full Allure suite/feature/story metadata
- ✔ JSON Schema validation
- ✔ Fixtures for data flow
- ✔ Chained tests (ZIP → GEO → WEATHER)
- ✔ Clean test code (request logic moved to endpoint classes)

### 🚧 In progress

- Parametrized test matrix
- Negative scenarios
- CI/CD (GitHub Actions)
- Logging system

---

## 📝 Roadmap

- [ ] Add negative tests
- [ ] Add broad parametrization
- [ ] Add GitHub Actions CI pipeline
- [ ] Add debug/info logging
- [ ] Add more endpoints (forecast, air pollution, etc.)

---

## 📄 License

MIT License

---

## 👤 Author

**Dmitrii Kiselev**

- GitHub: [@Didroi](https://github.com/Didroi)
- LinkedIn: [dmitrii-kiselev](https://linkedin.com/in/dmitrii-kiselev)

---

⭐ *If this project helped you — leave a star!*