from typing import List, Dict, Any


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция принимающая список словарей и опциональное значение для ключа
    state"""
    return [d for d in data if d.get("state") == state]


def sort_by_date(date_list: list, reverse_list: bool = True) -> list | bool:
    """Функция принимающая список словарей и параметр, задающий порядок сортировки (по умолчанию — убывание)"""
    sorted_list = sorted(date_list, key=lambda date_dict: date_dict.get("date"), reverse=reverse_list)
    return sorted_list
