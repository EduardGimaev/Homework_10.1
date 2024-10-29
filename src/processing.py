from typing import Any


def filter_by_state(list_dictionary: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция, фильтрующая словари по указанному параметру"""

    new_list = []

    for key in list_dictionary:
        if key.get("state") == state_id:
            new_list.append(key)
    return new_list


def sort_by_date(list_dictionary: list[dict[str, Any]], revers: bool = True) -> list[dict[str, Any]]:
    """Функция сортирующая список по дате"""

    sorted_list = sorted(list_dictionary, key=lambda x: x["date"], reverse=revers)
    return sorted_list
