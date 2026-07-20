"""
Модуль тестирования функций маскировки из модуля masks.

Содержит тесты для проверки корректности маскировки номеров карт и счетов.
"""

import pytest
from src.masks import get_mask_card_number, get_mask_account
from .fixtures.card_data import CARD_TEST_CASES, ACCOUNT_TEST_CASES  # Импорт данных


# def test_get_mask_account() -> None:
# # Тестирует функцию get_mask_account. Проверяет, что номер счета маскируется в формате **XXXX.
#     assert get_mask_account(ACCOUNT_NUMBER) == EXPECTED_ACCOUNT


@pytest.mark.parametrize("card_number, expected, description", CARD_TEST_CASES)
def test_get_mask_card_number(card_number, expected, description):

    """Тест с данными из отдельного Python-файла."""

    assert get_mask_card_number(card_number) == expected, (
        f"Ошибка в кейсе: {description} (номер: {card_number})"
    )


@pytest.mark.parametrize("account_number, expected, description", ACCOUNT_TEST_CASES)
def test_get_mask_account(account_number, expected, description) -> None:
    """
    Параметризованный тест маскировки номера счета.
    """
    assert get_mask_account(account_number) == expected, (
        f"Ошибка в кейсе: {description} (счет: {account_number})"
    )
# def test_get_mask_card_number() -> str:
#     assert get_mask_card_number(srt1) == srt1_1
#
#
# def test_get_mask_account() -> str:
#     assert get_mask_account(srt2) == srt2_2
