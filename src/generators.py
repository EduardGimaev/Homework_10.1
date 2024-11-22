from typing import Generator


def filter_by_currency(transaction_list, currency) -> Generator:
    """Функция возвращает транзакции по заданному параметру"""
    if transaction_list == []:
        raise StopIteration("Нет данных")
    else:
        for transaction in transaction_list:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
            else:
                continue


def transaction_descriptions(transaction_list):
    """Генератор возвращающий описание каждой операции по очереди"""
    for transaction in transaction_list:
        yield transaction["description"]


def card_number_generator(start, stop):
    """Функция, которая генерирует номер карты, в зависимости от указанного диапазона"""
    for number in range(start, stop):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield formatted_card_number


for card_number in card_number_generator(1, 20):
    print(card_number)
