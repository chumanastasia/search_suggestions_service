from fastapi import APIRouter, Depends, Query

from src.dependecies import get_cache_service, get_search_suggestions_service
from src.repositories.persons import RedisCache
from src.schemas import Person
from src.services.search_suggestions import SearchSuggestions

api_router = APIRouter()


@api_router.get("/suggestions")
async def suggestions(
    person: Person = Depends(),
    service: SearchSuggestions = Depends(get_search_suggestions_service),
    cache: RedisCache = Depends(get_cache_service),
):
    """Получает подсказки по запросу ФИО"""
    cached_suggests = cache.get(str(person))
    if cached_suggests is not None:
        return cached_suggests.split(",")
    suggests = await service.get_suggestions(person)
    cache.set(f"{person}", f'{", ".join(suggests)}', 60 * 60 * 24)
    return suggests
