import asyncio

import aiohttp
import orjson
from loguru import logger
from pydantic import validate_call

from src.schemas import Person, SuggestionConfig


class SearchSuggestions:
    """Класс для получения подсказок по запросу ФИО"""

    wizard_suggest: str = "Wizard_entity"
    suggestion_config: SuggestionConfig = SuggestionConfig()

    @validate_call
    async def get_suggestions_web(self, person: Person):
        """Получает все подсказки по запросу ФИО

        Args:
            person (Person): ФИО человека

        Returns:
            list: Список подсказок

        Raises:
            HTTPError: Ошибка при получении подсказок
        """
        request_url = self.suggestion_config.get_url(person)
        logger.debug(f"Make request url: {request_url}")
        async with aiohttp.ClientSession() as session:
            async with session.get(request_url) as response:
                response.raise_for_status()

                logger.success(f"Response status: {response.status}")
                return orjson.loads(await response.read())

    @validate_call
    async def check_wizard_suggestions(self, person: Person):
        """Проверяет наличие подсказок с типом Wizard_entity"""

        suggestions = await self.get_suggestions_web(person)
        _, second_suggestion, *_, last_suggestion = suggestions

        log_suggestions = last_suggestion.get("log")
        if log_suggestions is None:
            return ()

        count_wizard_suggest = log_suggestions.count(self.wizard_suggest)
        if count_wizard_suggest == 0:
            logger.info("Wizard_entity not found")
            return ()
        return second_suggestion[-count_wizard_suggest:]

    @validate_call
    async def get_suggestions(self, person: Person):
        """Возвращает список подсказок c типом Wizard_entity"""
        wizard_suggests = await self.check_wizard_suggestions(person)
        result = tuple(f"{ws_sg[1]} ({ws_sg[3]})" for ws_sg in wizard_suggests)
        logger.info(f"Found {len(result)} wizard_entity suggestions")
        return result
