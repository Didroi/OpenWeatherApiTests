from pydantic import BaseModel, Field
from typing import Optional


class GeoByLocationOrCoordinatesSchema(BaseModel):
    """
    Схема ответа: GET geo/1.0/direct и GET geo/1.0/reverse
    Получение геолокации по названию города. Получение данных по координатам
    """
    name: str = Field(..., description="Название локации")
    local_names: Optional[dict] = Field(None, description="Локальные названия")
    lat: float = Field(..., description="Широта")
    lon: float = Field(..., description="Долгота")
    country: str = Field(..., description="Код страны")
    state: Optional[str] = Field(None, description="Регион/штат")


class GeoByZipCodeSchema(BaseModel):
    """
    Схема ответа: GET geo/1.0/zip
    Получение геолокации по ZIP коду
    """
    zip: str = Field(..., description="Почтовый индекс")
    name: str = Field(..., description="Название локации")
    lat: float = Field(..., description="Широта")
    lon: float = Field(..., description="Долгота")
    country: str = Field(..., description="Код страны")
