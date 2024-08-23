import sys
from typing import Any, Generator


def filter_by_currency(transactions: list, currency_code: str = "USD") -> Generator[Any, Any, Any]:
    """Функция выдает транзакции соответствующей валютной операции."""
    if transactions == []:
        sys.exit("Нет транзакций")
    for key in transactions:
        if key.get("operationAmount").get("currency").get("code") != currency_code:
            sys.exit("В транзакциях нет такого кода")
        elif key.get("operationAmount").get("currency").get("code") == currency_code:
            yield key


def transaction_descriptions(transactions: list) -> Generator[Any, Any, Any]:
    """Функция принимает словари с транзакциями и поочередно возвращает описание операций."""
    if not transactions:
        sys.exit("Нет транзакций")
    for description_operation in transactions:
        yield description_operation.get("description")


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    """Функция генерирует номера карт в диапазоне от **0001 до **9999."""
    for x in range(start, stop + 1):
        zero_num = "0000000000000000"
        card_number = zero_num[: -len(str(x))] + str(x)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
