import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_details, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("", "Не корректный номер или счет"),
    ],
)
def test_mask_account_card(card_details: str, expected: str) -> None:
    assert mask_account_card(card_details) == expected


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:", "11.03.2024"),
        ("", "Не корректная дата"),
    ],
)
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected
