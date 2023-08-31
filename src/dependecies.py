import aiohttp
import redis
from fastapi import Depends

from src.repositories.persons import RedisCache
from src.services.search_suggestions import SearchSuggestions
from src.settings import RedisSettings

redis_settings = RedisSettings()


def get_search_suggestions_service() -> SearchSuggestions:
    return SearchSuggestions()


def get_redis_client() -> redis.Redis:
    return redis.from_url(str(redis_settings.dsn))


def get_cache_service(
    redis_client: redis.Redis = Depends(get_redis_client),
) -> RedisCache:
    return RedisCache(redis_client)
