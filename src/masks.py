def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскировки номера карты"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]}{card_number[4:6]}{'*' * 2}{'*' * 4}{card_number[12:]}"
    else:
        return None


def get_mask_account(account_number: str) -> str | None:
    """Функция маскировки номера счета"""
    if account_number.isdigit() and len(account_number) == 20:
        return f"{'*' * 2}{account_number[-4::]}"
    else:
        return None
