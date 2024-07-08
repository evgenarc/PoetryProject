from masks import get_mask_card_number, get_mask_account
import re

def mask_account_card(card_info: str) -> str:
    """Функция получает на вход данные о карте или счете и возвращает замаскированные данные
    """
    # Проверка на счет или банковскую карту
    hidden_info = ''
    if card_info.startswith("Счет"):
        account_number = re.search(r'\d{20}', card_info)
        if account_number:
            hidden_info = "Счет " + get_mask_account(account_number.group(0))
        else:
            hidden_info = "Неверный номер счета"
    else:
        card_number = re.search(r'\d{16}', card_info)
        if card_number:
            hidden_info = re.sub(r'\d{16}', get_mask_card_number(card_number.group(0)), card_info)
        else:
            hidden_info = "Неверный номер карты"

    return hidden_info


def get_data(date: str) -> str:
    """Принимает на вход строку с датой и возвращает ее в нужном формате"""
    only_date = re.search(r"\d{4}-\d{2}-\d{2}", date).group(0)
    year = only_date[:4]
    mounth = only_date[5:7]
    day = only_date[8:]
    return f"{day}.{mounth}.{year}"
