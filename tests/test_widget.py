"""
Модуль тестирования функций маскировки.
"""
import pytest
from src.widget import mask_account_card, get_date
from .fixtures.card_data import MASK_ACCOUNT_CARD_TEST_CASES, DATE_TEST_CASES # Импорт данных

@pytest.mark.parametrize(
    "card_info, expected, description",
    MASK_ACCOUNT_CARD_TEST_CASES,
    ids=[case[2] for case in MASK_ACCOUNT_CARD_TEST_CASES]
)
def test_mask_account_card(card_info, expected, description) -> None:
    """
    Параметризованный тест маскировки карты или счета с типом.
    """
    assert mask_account_card(card_info) == expected, (
        f"Ошибка в кейсе: {description} (входные данные: {card_info})"
    )

@pytest.mark.parametrize(
    "date_string, expected, description",
    DATE_TEST_CASES,
    ids=[case[2] for case in DATE_TEST_CASES]
)
def test_get_date(date_string, expected, description) -> None:
    """
    Параметризованный тест форматирования даты.
    """
    assert get_date(date_string) == expected, (
        f"Ошибка в кейсе: {description} (входная дата: {date_string})"
    )