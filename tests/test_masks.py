"""
Модуль тестирования функций маскировки из модуля masks.

Содержит тесты для проверки корректности маскировки номеров карт и счетов.
"""

# from .fixtures.card_data import ACCOUNT_TEST_CASES, CARD_TEST_CASES  # Импорт данных
# def test_get_mask_account() -> None:
# # Тестирует функцию get_mask_account. Проверяет, что номер счета маскируется в формате **XXXX.
#     assert get_mask_account(ACCOUNT_NUMBER) == EXPECTED_ACCOUNT


import pytest

# ✅ Правильный импорт - ИСПРАВЛЕНО!
from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number() -> None:
    """Тест маскировки номера карты."""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_mask_account() -> None:
    """Тест маскировки номера счета."""
    assert get_mask_account("73654108430135874305") == "** 4305"


def test_mask_card_no_number_invalid() -> None:
    """Тест на пустой номер карты."""
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_mask_card_number_invalid() -> None:
    """Тест на невалидный номер карты (слишком длинный)."""
    with pytest.raises(ValueError):
        get_mask_card_number("7000792289606361098776")


def test_mask_account_no_number_invalid() -> None:
    """Тест на пустой номер счета."""
    with pytest.raises(ValueError):
        get_mask_account("")


def test_mask_account_number_invalid() -> None:
    """Тест на невалидный номер счета (слишком длинный)."""
    with pytest.raises(ValueError):
        get_mask_account("70007922896063618758432098776")
