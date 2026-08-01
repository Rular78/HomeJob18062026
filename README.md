📋 Описание проекта
Проект HomeJob180626 представляет собой набор утилит для работы с банковскими транзакциями.
Включает функции для маскировки конфиденциальных данных, фильтрации, сортировки и генерации тестовых данных.

  Структура проекта:

  HomeJob180626/
├── src/                          # Исходный код
│   ├── masks.py                  # Маскировка номеров карт и счетов
│   ├── processing.py             # Фильтрация и сортировка транзакций
│   ├── widget.py                 # Основные функции виджета
│   └── generators.py             # Генераторы данных
├── tests/                        # Тесты
│   ├── fixtures/                 # Тестовые данные
│   │   ├── card_data.py          # Данные для маскировки
│   │   └── processing_data.py    # Данные для фильтрации/сортировки
│   ├── test_masks.py             # Тесты маскировки
│   ├── test_processing.py        # Тесты фильтрации/сортировки
│   ├── test_widget.py            # Тесты виджета
│   └── test_generators.py        # Тесты генераторов
├── main.py                       # Точка входа
├── requirements.txt              # Зависимости
├── README.md                     # Документация
└── .gitignore                    # Игнорируемые файлы

## Содержание
- [Inroduction] Разаработка на основное требований для прохождения обучения SKYPRO
- [Start of Work]18.06.26  начало работы
- [пайтест] Тестирование проходило на каждом этапе. результат /home/cust/PycharmProjects/HomeJob180626
- [Deploy и CI/CD](#deploy-и-ci/cd)  Да, да быстрее в продакшен, вернется доработками и тех. долгом
- [Contributing] Этот проект должен помочь автоматизации труда
- [To do]Делать и делать
- [Команда проекта] Avaya&Nice&Colabrio

## Технологии
- [Python](https://www.python.org/)
- ...

## Использование
подключим к ораклу
На баше мы напишем скрипт и автоматизируем.
Добавим в Крон
Логирование сдадим в какой нибудь забикс
Нагрузку протянем в графики графаны
но потом... а может докер контейнер...

Установите npm-пакет с помощью команды:
```sh
$ npm i your-awesome-plugin-name
```

И добавьте в свой проект:
```typescript
import { hi } from "your-awesome-plugin-name";

hi(); // Выведет в консоль "Привет!"
```

## Разработка

### Требования
Для установки и запуска проекта, необходим [NodeJS](https://nodejs.org/) v8+.

### Установка зависимостей
Для установки зависимостей, выполните команду:
```sh
$ npm i
```

### Запуск Development сервера
Чтобы запустить сервер для разработки, выполните команду:
```sh
npm start
```

### Создание билда
Чтобы выполнить production сборку, выполните команду: 
```sh
npm run build
```

## Тестирование
Какие инструменты тестирования использованы в проекте и как их запускать. Например:

Наш проект покрыт юнит-тестами Jest. Для их запуска выполните команду:
```sh
npm run test
```

## Deploy и CI/CD
Расскажите, как развернуть приложение. Как запустить пайплайны и т.д.

## Contributing
Как помочь в разработке проекта?
Как отправить предложение или баг-репорт.
Как отправить доработку (оформить pull request, какие стайлгайды используются).
Можно вынести в отдельный файл — [Contributing.md](./CONTRIBUTING.md).

## FAQ 
Если потребители вашего кода часто задают одни и те же вопросы, добавьте ответы на них в этом разделе.

### Зачем вы разработали этот проект?
По заданию чтобы научиться и...
Много денег, машина, – все дела.(Чиж и компания)


## To do
- [x] Добавить крутое README
- [ ] Всё переписать
- [ ] ...

## Команда проекта
Оставьте пользователям контакты и инструкции, как связаться с командой разработки.

- RuLar78@rambler.ru

## Источники
https://my.sky.pro

кратко о функциях (очень полезно)

SRC
!!!!!!!!!!
masks.py
def get_mask_card_number(card_number: int | str) -> str:
***показывает от номера карты только 4 цифры
def get_mask_account(account_number: int | str) -> str:
***показывает от 20 значного номера счета только 4 цифры

!!!!!!!!!!
processing.py
def filter_by_state(data_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
***
def sort_by_date(data_list: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
***

!!!!!!!!!!
widget.py
def mask_account_card(card_info: str) -> str:
***
def get_date(date_string: str) -> str:
***

!!!!!!!!!!
generators.py
def filter_by_currency(transactions: list, currency_code: str = "USD") -> list:
***
def transaction_descriptions(transactions: list) -> Generator[Any, Any, Any]:
***
def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
***

TESTS
!!!!!!!!!!
fixtures ДИРЕКТОРИЯ
__init__.py
processing_data.py
переменная TRANSACTIONS {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}
переменная FILTER_BY_STATE_TEST_CASES (непонятный пока формат)
переменная SORT_BY_DATE_TEST_CASES (непонятный пока формат)
card_data.py
переменная CARD_TEST_CASES Данные для маскировки карт (функция get_mask_card_number)
переменная ACCOUNT_TEST_CASES Данные для маскировки счетов (функция get_mask_account)


__init__.py
widget.py (содержит обращения к функциям из masks.py)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number
def mask_account_card(card_info: str) -> str:    "Maestro 1596837868705199"-> 2201 38** **** 0013
def get_date(date_string: str) -> str:           "2024-03-11T02:26:18.671407"-> 11.03.2024

masks.py!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def get_mask_card_number(card_number: int | str) -> str:    1234567890123456-> 2201 38** **** 0013
def get_mask_account(account_number: int | str) -> str:     1234567890123456-> ** 3456

processing.py
from datetime import datetime
from typing import Any, Dict, List
def filter_by_state(data_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
принимает список словарей и опционально значение для ключа state
возвращает список словарей у которых ключ state соответствует указанному значению
пример заремленный в файле
def sort_by_date(data_list: List[Dict[str, Any]], is_descending: bool = True) -> List[Dict[str, Any]]:

generators.py
import sys
from typing import Any, Generator
def filter_by_currency(transactions: list, currency_code: str = "USD") -> list:
def transaction_descriptions(transactions: list) -> Generator[Any, Any, Any]:   получает список словарей, и выводит только заданное поле description
def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
примеры от отработаны test\generators.py


test_processing.py
import pytest
from typing import List, Dict, Any
from src.processing import filter_by_state, sort_by_date
from .fixtures.processing_data import FILTER_BY_STATE_TEST_CASES, SORT_BY_DATE_TEST_CASES
@pytest.mark.parametrize(
    "data_list, state, expected, description",
    FILTER_BY_STATE_TEST_CASES,
    ids=[case[3] for case in FILTER_BY_STATE_TEST_CASES],
)
@pytest.mark.parametrize(
    "data_list, is_descending, expected, description",
    SORT_BY_DATE_TEST_CASES,
    ids=[case[3] for case in SORT_BY_DATE_TEST_CASES],
)
def test_filter_by_state(data_list: List[Dict[str, Any]], state: str, expected: List[Dict[str, Any]], description: str) -> None:
def test_sort_by_date(data_list: List[Dict[str, Any]], is_descending: bool, expected: List[Dict[str, Any]], description: str) -> None:

test_widget.py
import pytest
from src.widget import get_date, mask_account_card
from .fixtures.card_data import DATE_TEST_CASES, MASK_ACCOUNT_CARD_TEST_CASES
@pytest.mark.parametrize(
    "card_info, expected, description",
    MASK_ACCOUNT_CARD_TEST_CASES,
    ids=[case[2] for case in MASK_ACCOUNT_CARD_TEST_CASES],
)
@pytest.mark.parametrize(
    "date_string, expected, description",
    DATE_TEST_CASES,
    ids=[case[2] for case in DATE_TEST_CASES]
def test_mask_account_card(card_info: str, expected: str, description: str) -> None:
def test_get_date(date_string: str, expected: str, description: str) -> None:

test_mask.py
import pytest
from src.masks import get_mask_card_number, get_mask_account
def test_mask_card_number() -> None:
def test_mask_account() -> None:
def test_mask_card_no_number_invalid() -> None:
def test_mask_card_number_invalid() -> None:
def test_mask_account_no_number_invalid() -> None:
def test_mask_account_number_invalid() -> None:

test_masks.py
import pytest
from your_module import get_mask_card_number, get_mask_account
from your_test_data import CARD_TEST_CASES, ACCOUNT_TEST_CASES
@pytest.mark.parametrize("card_number, expected, description", CARD_TEST_CASES)
@pytest.mark.parametrize("account_number, expected, description", ACCOUNT_TEST_CASES)
def test_get_mask_card_number(card_number: str, expected: str, description: str) -> None:
def test_get_mask_account(account_number: str, expected: str, description: str) -> None:

test_generators.py
from typing import List, Generator, Iterator
import pytest
from src.generators import transaction_descriptions, card_number_generator

def test_transaction_descriptions_3(index: int, expected: str) -> None:
def test_transaction_descriptions_zero() -> None:
def test_card_number_generator() -> None:
def test_card_number_generator_beginning() -> None:
def test_card_number_generator_end() -> None:
descriptions = transaction_descriptions(transactions)


@pytest.mark.parametrize("card_number, expected, description", CARD_TEST_CASES)
параметризованный тест с данными из CARD_TEST_CASES
Храните тестовые данные в папке tests/fixtures/ - это стандартная практика