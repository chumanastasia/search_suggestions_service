from typing import ClassVar

from pydantic import BaseModel, Field, HttpUrl, PositiveInt, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class MixInSettings(BaseSettings):
    """Класс настроек для миксинов."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


class AppSettings(MixInSettings):
    """Класс настроек приложения из переменных окружения."""

    host: str = Field(default="0.0.0.0")
    port: PositiveInt = Field(default=8000)


class RedisSettings(MixInSettings):
    """Класс настроек Redis из переменных окружения."""

    dsn: RedisDsn = Field(default="redis://localhost:6379")
    ttl: PositiveInt = Field(default=60 * 60 * 24)
