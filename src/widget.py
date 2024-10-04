from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_details: str) -> str:
    """Функция, которая маскирует номера карты либо счета"""
    if len(card_details.split()[-1]) == 16:
        card_details_new = get_mask_card_number(card_details.split()[-1])
        result = f"{card_details[:-16]}{card_details_new}"
    else:
        new_number = get_mask_account(card_details.split()[-1])
        result = f"{card_details[:-20]}{new_number}"
    return result


def get_date(date: str) -> str:
    """Функция, которая возвращает дату в формате 'ДД.ММ.ГГГГ'"""
    new_date = date[0:10].split("-")
    return ".".join(new_date[::-1])
