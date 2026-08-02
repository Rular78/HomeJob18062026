"""
Модуль masks ля демонстрации работы функций маскировки.

Требование к задачам 9.1

Содержит функции для маскировки номеров карт и счетов.
"""


def get_mask_card_number(card_number: int | str) -> str:
    card_number = str(card_number)
    print("работает функция get_mask_card_number")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: int | str) -> str:
    account_number = str(account_number)
    print("работает функция get_mask_account")
    return f"** {account_number[-4:]}"


# print(get_mask_account("1234567890123456"))
# print("отработала функция get_mask_account")
print(get_mask_card_number("2201382000000013"))
