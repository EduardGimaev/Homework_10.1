from src.masks import get_mask_account, get_mask_card_number
import pytest

@pytest.mark.parametrize("card_number, expected", [
    ("2200358209833331", "2200 35** **** 3331"),
    ("9833331", "Номер карты указан неверно"),
    ("a200358209833331", "Номер карты указан неверно"),
    ("", "Номер карты указан неверно")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("56873457634785634876", "**4876"),
    ("568734576", "Номер счета указан неверно"),
    ("", "Номер счета указан неверно")
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
