from src.masks import get_mask_card_number, get_mask_account


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

result1 = mask_account_card("Visa Platinum 7000792289606361")
print(result1)  # Visa Platinum 7000 79** **** 6361