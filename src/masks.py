def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""

    card_number_str = str(card_number)
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""

    account_number_str = str(account_number)
    return f"**{account_number_str[-4:]}"
