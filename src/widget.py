from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(card_info: str) -> str:

    # Разделяем строку на части: тип и номер
    parts = card_info.rsplit(' ', 1)  # Разделяем по последнему пробелу

    # Если разделение не удалось (нет пробела), возвращаем исходную строку
    if len(parts) != 2:
        return card_info

    card_type = parts[0]  # Тип: "Visa Platinum" или "Счет"
    card_number = parts[1]  # Номер: "7000792289606361"

    # Определяем тип по ключевым словам
    if "Счет" in card_type:
        # Для счетов используем get_mask_account
        masked_number = get_mask_account(card_number)
    else:
        # Для карт используем get_mask_card_number
        masked_number = get_mask_card_number(card_number)

    # Возвращаем результат: тип + замаскированный номер
    return f"{card_type} {masked_number}"


def get_date(date_string: str) -> str:

    # Парсим строку в объект datetime
    dt = datetime.fromisoformat(date_string)

    # Возвращаем в нужном формате
    return dt.strftime("%d.%m.%Y")

# result1 = mask_account_card("Maestro 1596837868705199")
# print(result1)
# result1 = mask_account_card("Счет 64686473678894779589")
# print(result1)
# result1 = mask_account_card("MasterCard 7158300734726758")
# print(result1)
# result1 = mask_account_card("Счет 35383033474447895560")
# print(result1)
# result1 = mask_account_card("Visa Classic 6831982476737658")
# print(result1)
# result1 = mask_account_card("Visa Platinum 8990922113665229")
# print(result1)
# result1 = mask_account_card("Visa Gold 5999414228426353")
# print(result1)
# result1 = mask_account_card("Счет 73654108430135874305")
# print(result1)

result1 = get_date("2026-03-11T02:26:18.671407")
print(result1)


