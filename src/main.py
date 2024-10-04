from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    print(get_mask_card_number("2200358209833331"))
    print(get_mask_account("56873457634785634876"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(get_date("2024-03-11T02:"))
