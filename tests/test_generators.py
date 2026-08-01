from typing import Generator, Iterator, List

import pytest

from src.generators import card_number_generator, transaction_descriptions

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


# def test_filter_by_currency():
#    generator = filter_by_currency(transactions)
#    assert next(generator) == {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
#                               'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
#                               'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
#                               'to': 'Счет 11776614605963066702'}


# def test_filter_by_currency_zero():
#    with pytest.raises(SystemExit, match="Нет транзакций") as exc_info:
#        generator = filter_by_currency([])
#        assert next(generator) == exc_info


# def test_filter_by_currency_eu():
#    with pytest.raises(SystemExit, match="В транзакциях нет такого кода") as exc_info:
#        generator = filter_by_currency(transactions, 'EU')
#        assert next(generator) == exc_info


@pytest.mark.parametrize(
    "index, expected",
    [
        (0, "Перевод организации"),
        (1, "Перевод со счета на счет"),
        (2, "Перевод со счета на счет"),
        (3, "Перевод с карты на карту"),
        (4, "Перевод организации"),
    ],
)
def test_transaction_descriptions_3(index: int, expected: str) -> None:
    """Тест получения описания транзакции по индексу."""
    descriptions: List[str] = list(transaction_descriptions(transactions))
    assert descriptions[index] == expected


def test_transaction_descriptions_zero() -> None:
    """Тест на пустой список транзакций."""
    with pytest.raises(SystemExit, match="Нет транзакций") as exc_info:
        a: Generator[str, None, None] = transaction_descriptions([])
        assert next(a) == exc_info


def test_card_number_generator() -> None:
    """Тест генератора номеров карт."""
    numer: Iterator[str] = card_number_generator(95, 96)
    assert next(numer) == "0000 0000 0000 0095"


def test_card_number_generator_beginning() -> None:
    """Тест генератора с начальным значением 0."""
    numer: Iterator[str] = card_number_generator(0, 1)
    assert next(numer) == "0000 0000 0000 0000"


def test_card_number_generator_end() -> None:
    """Тест генератора с максимальным значением."""
    numer: Iterator[str] = card_number_generator(9999999999999999, 9999999999999999)
    assert next(numer) == "9999 9999 9999 9999"


#
# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))
#
# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions))
