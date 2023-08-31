from typing import ClassVar

from pydantic import BaseModel, Field, HttpUrl, PositiveInt, constr


class Person(BaseModel):
    """Модель данных для человека."""

    first_name: constr(min_length=1, max_length=50) = Field(
        default="Иван",
        description="Имя человека",
        example="Иван",
    )
    last_name: constr(min_length=1, max_length=50) = Field(
        default="Иванов",
        description="Фамилия человека",
        example="Иванов",
    )
    patronymic: constr(min_length=1, max_length=50) = Field(
        default="Иванович",
        description="Отчество человека",
        example="Иванович",
    )

    def __str__(self) -> str:
        """Возвращает ФИО человека."""
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    __repr__ = __str__


class SuggestionConfig(BaseModel):
    """Конфиг для получения подсказок по запросу ФИО."""

    host: ClassVar[HttpUrl] = "https://ya.ru"
    path: ClassVar[str] = "/suggest/suggest-ya.cgi"
    params_pattern: ClassVar[
        str
    ] = "v={v}&entity_enrichment={entity_enrichment}&part={l_name} {f_name} {patronymic}"

    @classmethod
    def get_url(
        cls,
        person: Person,
        version: PositiveInt = 4,
        entity_enrichment: PositiveInt = 1,
    ) -> str:
        """Возвращает url для получения подсказок по запросу ФИО."""
        url_pattern = "{host}{path}?{params}"

        params = cls.params_pattern.format(
            v=version,
            entity_enrichment=entity_enrichment,
            l_name=person.last_name,
            f_name=person.first_name,
            patronymic=person.patronymic,
        )

        return url_pattern.format(
            host=cls.host,
            path=cls.path,
            params=params,
        )
