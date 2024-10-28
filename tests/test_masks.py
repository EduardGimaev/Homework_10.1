from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("2200358209833331") == "2200 35** **** 3331"
    assert get_mask_card_number("9833331") == "Номер карты указан неверно"
    assert get_mask_card_number("a200358209833331") == "Номер карты указан неверно"
    assert get_mask_card_number("") == "Номер карты указан неверно"


def test_get_mask_account():
    assert get_mask_account("56873457634785634876") == "**4876"
    assert get_mask_account("568734576") == "Номер счета указан неверно"
    assert get_mask_account("") == "Номер счета указан неверно"




