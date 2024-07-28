def filter_by_state(data, state="EXECUTED"):
    """Функция принимающая список словарей и опциональное значение для ключа
    state"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data, reverse=True):
    """Функция принимающая список словарей и параметр, задающий порядок сортировки (по умолчанию — убывание)"""
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
