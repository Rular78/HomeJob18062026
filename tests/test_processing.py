from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date

"""
#from datetime import datetime
#from typing import Any, Dict, List
"""
from .fixtures.processing_data import FILTER_BY_STATE_TEST_CASES, SORT_BY_DATE_TEST_CASES

TRANSACTIONS = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


@pytest.mark.parametrize(
    "data_list, state, expected, description",
    FILTER_BY_STATE_TEST_CASES,
    ids=[case[3] for case in FILTER_BY_STATE_TEST_CASES],
)
def test_filter_by_state(
    data_list: List[Dict[str, Any]], state: str, expected: List[Dict[str, Any]], description: str
) -> None:
    """
    Параметризованный тест фильтрации транзакций по состоянию.
    """
    assert filter_by_state(data_list, state) == expected, f"Ошибка в кейсе: {description}"


@pytest.mark.parametrize(
    "data_list, is_descending, expected, description",
    SORT_BY_DATE_TEST_CASES,
    ids=[case[3] for case in SORT_BY_DATE_TEST_CASES],
)
def test_sort_by_date(
    data_list: List[Dict[str, Any]], is_descending: bool, expected: List[Dict[str, Any]], description: str
) -> None:
    """
    Параметризованный тест сортировки транзакций по дате.
    """
    assert sort_by_date(data_list, is_descending) == expected, f"Ошибка в кейсе: {description}"
