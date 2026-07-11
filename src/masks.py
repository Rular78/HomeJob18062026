from src import masks


def get_mask_card_number(card_number: int | str) -> str:
    # 1. Сначала преобразуем в строку и убираем пробелы
    card_number = str(card_number).replace(" ", "")

    # 2. Проверяем: только цифры
    if not card_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    # 3. Проверяем: ровно 16 цифр
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр")

    # 4. Маскируем
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: int | str) -> str:
    # 1. Преобразуем в строку и убираем пробелы
    account_number = str(account_number).replace(" ", "")

    # 2. Проверяем: только цифры
    if not account_number.isdigit():
        raise ValueError("Номер счёта должен содержать только цифры")

    # 3. Проверяем: ровно 20 цифр
    if len(account_number) != 20:
        raise ValueError("Номер счёта должен содержать ровно 20 цифр")

    # 4. Маскируем (показываем только последние 4 цифры)
    return f"** {account_number[-4:]}"


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
