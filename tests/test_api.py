import pytest

import src.repositories.persons
from src.schemas import Person
from tests import testdata


@pytest.mark.asyncio
@pytest.mark.usefixtures("mock_cache_get_none", "mock_suggestions_request")
@pytest.mark.usefixtures("mock_suggestions_request")
async def test_suggestions_success(search_suggestions_service):
    response = await search_suggestions_service.get_suggestions(
        Person(
            last_name=testdata.PERSON_LAST_NAME,
            first_name=testdata.PERSON_FIRST_NAME,
            patronymic=testdata.PERSON_MIDDLE_NAME,
        )
    )
    assert response == ("Исаак Ильич Левитан (Русский живописец)",)


@pytest.mark.asyncio
@pytest.mark.usefixtures(
    "mock_cache_get_none", "mock_suggestions_request_no_wizard_entity"
)
async def test_suggestions_no_wizard_entity(search_suggestions_service):
    response = await search_suggestions_service.get_suggestions(
        Person(
            last_name=testdata.PERSON_LAST_NAME,
            first_name=testdata.PERSON_FIRST_NAME,
            patronymic=testdata.PERSON_MIDDLE_NAME,
        )
    )
    assert response == ()


@pytest.mark.asyncio
@pytest.mark.usefixtures("mock_cache_get_none", "mock_suggestions_request_no_log")
async def test_suggestions_no_log(search_suggestions_service):
    response = await search_suggestions_service.get_suggestions(
        Person(
            last_name=testdata.PERSON_LAST_NAME,
            first_name=testdata.PERSON_FIRST_NAME,
            patronymic=testdata.PERSON_MIDDLE_NAME,
        )
    )
    assert response == ()
