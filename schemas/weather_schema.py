from typing import Optional, List

from pydantic import BaseModel, Field


class CoordSchema(BaseModel):
    """Координаты локации"""
    lon: float = Field(..., description="Долгота")
    lat: float = Field(..., description="Широта")


class WeatherConditionSchema(BaseModel):
    """Погодные условия"""
    id: int = Field(..., description="ID погодного условия")
    main: str = Field(..., description="Группа погодных параметров (Rain, Snow, Clouds)")
    description: str = Field(..., description="Описание погоды")
    icon: str = Field(..., description="Иконка погоды")


class MainWeatherSchema(BaseModel):
    """Основные параметры погоды"""
    temp: float = Field(..., description="Температура")
    feels_like: float = Field(..., description="Ощущается как")
    temp_min: float = Field(..., description="Минимальная температура")
    temp_max: float = Field(..., description="Максимальная температура")
    pressure: int = Field(..., description="Атмосферное давление, hPa")
    humidity: int = Field(..., description="Влажность, %")
    sea_level: Optional[int] = Field(None, description="Давление на уровне моря, hPa")
    grnd_level: Optional[int] = Field(None, description="Давление на уровне земли, hPa")


class WindSchema(BaseModel):
    """Информация о ветре"""
    speed: float = Field(..., description="Скорость ветра")
    deg: int = Field(..., description="Направление ветра, градусы")
    gust: Optional[float] = Field(None, description="Порывы ветра")


class CloudsSchema(BaseModel):
    """Информация об облачности"""
    all: int = Field(..., description="Облачность, %")


class SysSchema(BaseModel):
    """Системная информация"""
    type: Optional[int] = Field(None, description="Внутренний параметр")
    id: Optional[int] = Field(None, description="Внутренний параметр")
    country: str = Field(..., description="Код страны")
    sunrise: int = Field(..., description="Время восхода, unix UTC")
    sunset: int = Field(..., description="Время заката, unix UTC")


class CurrentWeatherSchema(BaseModel):
    """
    Схема ответа: GET data/2.5/weather
    Получение текущей погоды
    """
    coord: CoordSchema = Field(..., description="Координаты")
    weather: List[WeatherConditionSchema] = Field(..., description="Погодные условия")
    base: str = Field(..., description="Внутренний параметр")
    main: MainWeatherSchema = Field(..., description="Основные параметры погоды")
    visibility: int = Field(..., description="Видимость, метры")
    wind: WindSchema = Field(..., description="Ветер")
    clouds: CloudsSchema = Field(..., description="Облачность")
    dt: int = Field(..., description="Время расчёта данных, unix UTC")
    sys: SysSchema = Field(..., description="Системная информация")
    timezone: int = Field(..., description="Сдвиг в секундах от UTC")
    id: int = Field(..., description="ID города")
    name: str = Field(..., description="Название города")
    cod: int = Field(..., description="Внутренний параметр")
