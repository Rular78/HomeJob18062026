import pytest

@pytest.fixture
def sample_transactions():
    """Фикстура с примерами транзакций."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-02T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03T15:30:00"},
    ]

# test_processing.py
def test_filter_by_state(sample_transactions):
    result = filter_by_state(sample_transactions, "EXECUTED")
    assert len(result) == 2