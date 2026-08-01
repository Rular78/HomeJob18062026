import sys
from typing import Any, Generator


def filter_by_currency(transactions: list, currency_code: str = "USD") -> list:
    """Функция выдает транзакции, где валюта операции соответствует заданной."""
    # if transactions == []:
    #    sys.exit("Нет транзакций")
    transactions_code = []
    for i in transactions:
        if i.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency_code:
            transactions_code.append(i)
        elif i.get('currency_code') == currency_code:
            transactions_code.append(i)
    return transactions_code


def transaction_descriptions(transactions: list) -> Generator[Any, Any, Any]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    if not transactions:
        sys.exit("Нет транзакций")
    for description_operation in transactions:
        yield description_operation.get("description")


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    """Функция может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for x in range(start, stop + 1):
        number_zero = "0000000000000000"
        card_number = number_zero[: -len(str(x))] + str(x)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"


transaction_list1 = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
]
# usd_transactions = filter_by_currency(transaction_list1,"USD")
# print(usd_transactions)
# usd_transactions = filter_by_currency(transaction_list1,"RUB")
# print(usd_transactions)
# descriptions = transaction_descriptions(transaction_list1)
# for _ in range(2):  #  нужно учитывать сколько уникальных словарей в списке
#     print(next(descriptions))
# for card in card_number_generator(9999999999999995, 9999999999999999):
#     print(card)
# gen = card_number_generator(95, 95)
# print(next(gen))
