"""
Модуль processing  для демонстрации работы функций фильтрации списков

Требование к задачам 10.1

Содержит функции для фильтрации списка словарей и сортировке словаря по дате
"""

from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data_list: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    return [item for item in data_list if item.get('state') == state]


def sort_by_date(data_list: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    # Функция для извлечения даты из словаря с преобразованием в объект datetime
    def get_date(item: Dict[str, Any]) -> datetime:
        date_str = item.get('date', '')
        try:
            # Парсим строку с датой в формате ISO 8601
            return datetime.fromisoformat(date_str)
        except (ValueError, TypeError):
            # Если дата отсутствует или имеет неверный формат, возвращаем минимальную дату
            # чтобы такие записи оказались в конце списка
            return datetime.min
    return sorted(data_list, key=get_date, reverse=descending)


# transactions = [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]
# executed = filter_by_state(transactions)
# for item in executed:
#     print(f"  {item}")
transactions1 = [
      {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
sorted_asc = sort_by_date(transactions1, True)
for item in sorted_asc:
    print(f"  {item}")
