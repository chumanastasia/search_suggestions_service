from functools import wraps

import redis
from loguru import logger
from pydantic import PositiveInt, validate_call


class RedisCache:
    def __init__(self, redis_client: redis.Redis):
        self.redis_client = redis_client

    @validate_call
    def get(self, cache_key: str) -> str | None:
        """Возвращает значение по ключу"""
        cached_value = self.redis_client.get(cache_key)
        if cached_value is None:
            logger.info(f"Key [{cache_key}] not found in cache")
            return None
        logger.info(f"Key [{cache_key}] found in cache")
        return cached_value.decode("utf-8")

    @validate_call
    def set(self, cache_key: str, cached_value: str, ttl: PositiveInt | None = None):
        """Сохраняет значение по ключу"""
        self.redis_client.set(cache_key, cached_value, ex=ttl)
        logger.info(f"Key [{cache_key}] set in cache")
