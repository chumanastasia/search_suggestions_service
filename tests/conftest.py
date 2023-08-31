import urllib
from http import HTTPStatus
from unittest import mock

import pytest
from aioresponses import aioresponses

from src.services.search_suggestions import SearchSuggestions
from src.settings import AppSettings
from tests import testdata


@pytest.fixture
def mock_session() -> aioresponses:
    with aioresponses() as session:
        yield session


@pytest.fixture
def mock_cache_get_none() -> None:
    mock.patch("src.repositories.persons.RedisCache.get", return_value=None)
    mock.patch("src.repositories.persons.RedisCache.set", return_value=None)


@pytest.fixture
def search_suggestions_service() -> SearchSuggestions:
    yield SearchSuggestions()


@pytest.fixture
def mock_suggestions_request(mock_session: aioresponses) -> None:
    part = "&part={last_name} {first_name} {patronymic}".format(
        last_name=testdata.PERSON_LAST_NAME,
        first_name=testdata.PERSON_FIRST_NAME,
        patronymic=testdata.PERSON_MIDDLE_NAME,
    )
    request_url = "{host}{path}".format(
        host="https://ya.ru",
        path=f"/suggest/suggest-ya.cgi?v=4&entity_enrichment=1&part={part}",
    )

    mock_session.get(
        url=request_url,
        status=HTTPStatus.OK.value,
        payload=testdata.RESPONSE_SUCCESS,
    )


@pytest.fixture
def mock_suggestions_request_no_wizard_entity(mock_session: aioresponses) -> None:
    part = "&part={last_name} {first_name} {patronymic}".format(
        last_name=testdata.PERSON_LAST_NAME,
        first_name=testdata.PERSON_FIRST_NAME,
        patronymic=testdata.PERSON_MIDDLE_NAME,
    )
    request_url = "{host}{path}".format(
        host="https://ya.ru",
        path=f"/suggest/suggest-ya.cgi?v=4&entity_enrichment=1&part={part}",
    )

    mock_session.get(
        url=request_url,
        status=HTTPStatus.OK.value,
        payload=testdata.RESPONSE_NO_WIZARD_ENTITY,
    )


@pytest.fixture
def mock_suggestions_request_no_log(mock_session: aioresponses) -> None:
    part = "&part={last_name} {first_name} {patronymic}".format(
        last_name=testdata.PERSON_LAST_NAME,
        first_name=testdata.PERSON_FIRST_NAME,
        patronymic=testdata.PERSON_MIDDLE_NAME,
    )
    request_url = "{host}{path}".format(
        host="https://ya.ru",
        path=f"/suggest/suggest-ya.cgi?v=4&entity_enrichment=1&part={part}",
    )

    mock_session.get(
        url=request_url,
        status=HTTPStatus.OK.value,
        payload=testdata.RESPONSE_NO_LOG,
    )
