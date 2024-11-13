import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize("descriptions", ["Перевод организации"])

def test_transaction_descriptions(transaction_list, descriptions):
    """Функция тестирует выдачу списка описания операций"""
    trans = transaction_descriptions(transaction_list)
    assert next(trans) == descriptions


def test_filter_by_currency(transaction_list, description):
    """"Функция тестирует выдачу операций по названию валют"""
    assert list(filter_by_currency(transaction_list, "USD")) == description


def test_card_number_generator():
    """Функция тестирует генератор номеров карт"""
    card_number = card_number_generator(9999999999999995, 9999999999999999)
    assert next(card_number) == "9999 9999 9999 9995"
    assert next(card_number) == "9999 9999 9999 9996"
