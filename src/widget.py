import re


def mask_account_card(card_info: str) -> str:
    """Функция получает на вход данные о карте или счете и возвращает замаскированные данные"""
    # Проверка на счет или банковскую карту
    hidden_info = ""
    if card_info[0:4] == "Счет":
        hidden_info = "Счет **" + card_info[-4:]
    else:
        first_part = re.search(r".+\s\d{6}", card_info).group(0)
        second_part = re.search(r"\d{4}$", card_info).group(0)

        hidden_info = f"{first_part}******{second_part}"
    return hidden_info


def get_data(date: str) -> str:
    """Принимает на вход строку с датой и возвращает ее в нужном формате"""
    only_date = re.search(r"\d{4}-\d{2}-\d{2}", date).group(0)
    year = only_date[:4]
    mounth = only_date[5:7]
    day = only_date[8:]
    return f"{day}.{mounth}.{year}"
