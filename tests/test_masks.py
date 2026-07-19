"""
Модуль тестирования функций маскировки из модуля masks.

Содержит тесты для проверки корректности маскировки номеров карт и счетов.
"""

from src.masks import get_mask_account, get_mask_card_number

# Тестовые данные
CARD_NUMBER = "7000792289606361"
EXPECTED_CARD = "7000 79** **** 6361"

ACCOUNT_NUMBER = "73654108430135874305"
EXPECTED_ACCOUNT = "**4305"  # Обрати внимание: без пробела, как в твоей функции


def test_get_mask_card_number() -> None:
    """
    Тестирует функцию get_mask_card_number.

    Проверяет, что номер карты маскируется в формате XXXX XX** **** XXXX.
    """
    assert get_mask_card_number(CARD_NUMBER) == EXPECTED_CARD


def test_get_mask_account() -> None:
    """
    Тестирует функцию get_mask_account.

    Проверяет, что номер счета маскируется в формате **XXXX.
    """
    assert get_mask_account(ACCOUNT_NUMBER) == EXPECTED_ACCOUNT


# def test_get_mask_card_number() -> str:
#     assert get_mask_card_number(srt1) == srt1_1
#
#
# def test_get_mask_account() -> str:
#     assert get_mask_account(srt2) == srt2_2
