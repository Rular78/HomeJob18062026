# Данные для фильтрации по состоянию (функция filter_by_state)
TRANSACTIONS = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

FILTER_BY_STATE_TEST_CASES = [
    # Фильтрация по умолчанию (EXECUTED)
    (
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "CANCELED"},
            {"id": 3, "state": "EXECUTED"},
            {"id": 4, "state": "PENDING"},
        ],
        "EXECUTED",
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 3, "state": "EXECUTED"},
        ],
        "Фильтр по умолчанию (EXECUTED)",
    ),
    # Фильтрация по CANCELED
    (
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "CANCELED"},
            {"id": 3, "state": "EXECUTED"},
            {"id": 4, "state": "CANCELED"},
        ],
        "CANCELED",
        [
            {"id": 2, "state": "CANCELED"},
            {"id": 4, "state": "CANCELED"},
        ],
        "Фильтр по CANCELED",
    ),
    # Фильтрация по PENDING (нет таких)
    (
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "CANCELED"},
        ],
        "PENDING",
        [],
        "Фильтр по PENDING (пустой результат)",
    ),
    # Пустой список
    ([], "EXECUTED", [], "Пустой список"),
    # Словари без ключа state
    (
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "name": "test"},
            {"id": 3, "state": "EXECUTED"},
        ],
        "EXECUTED",
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 3, "state": "EXECUTED"},
        ],
        "Словари без ключа state",
    ),
    # Фильтрация с другим состоянием
    (
        [
            {"id": 1, "state": "COMPLETED"},
            {"id": 2, "state": "COMPLETED"},
            {"id": 3, "state": "CANCELED"},
        ],
        "COMPLETED",
        [
            {"id": 1, "state": "COMPLETED"},
            {"id": 2, "state": "COMPLETED"},
        ],
        "Фильтр по COMPLETED",
    ),
]

SORT_BY_DATE_TEST_CASES = [
    # Сортировка по убыванию (по умолчанию)
    (
        TRANSACTIONS,
        True,
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
        "Сортировка по убыванию (сначала новые)",
    ),
    # Сортировка по возрастанию
    (
        TRANSACTIONS,
        False,
        [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ],
        "Сортировка по возрастанию (сначала старые)",
    ),
    # Сортировка с одинаковыми датами
    (
        [
            {"id": 1, "date": "2023-01-01T10:00:00"},
            {"id": 2, "date": "2023-01-01T10:00:00"},
            {"id": 3, "date": "2023-01-02T10:00:00"},
        ],
        True,
        [
            {"id": 3, "date": "2023-01-02T10:00:00"},
            {"id": 1, "date": "2023-01-01T10:00:00"},
            {"id": 2, "date": "2023-01-01T10:00:00"},
        ],
        "Сортировка с одинаковыми датами (порядок сохраняется)",
    ),
    # Пустой список
    ([], True, [], "Пустой список"),
    # Один элемент
    ([{"id": 1, "date": "2023-01-01T10:00:00"}], True, [{"id": 1, "date": "2023-01-01T10:00:00"}], "Один элемент"),
    # Словари без ключа date
    (
        [
            {"id": 1, "date": "2023-01-01T10:00:00"},
            {"id": 2, "name": "test"},
            {"id": 3, "date": "2023-01-02T10:00:00"},
        ],
        True,
        [
            {"id": 3, "date": "2023-01-02T10:00:00"},
            {"id": 1, "date": "2023-01-01T10:00:00"},
            {"id": 2, "name": "test"},
        ],
        "Словари без ключа date (в конце)",
    ),
    # Неверный формат даты
    (
        [
            {"id": 1, "date": "2023-01-01T10:00:00"},
            {"id": 2, "date": "invalid"},
            {"id": 3, "date": "2023-01-02T10:00:00"},
        ],
        True,
        [
            {"id": 3, "date": "2023-01-02T10:00:00"},
            {"id": 1, "date": "2023-01-01T10:00:00"},
            {"id": 2, "date": "invalid"},
        ],
        "Неверный формат даты (в конце)",
    ),
]
