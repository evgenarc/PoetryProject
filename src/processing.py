def filter_by_state(data, state="EXECUTED"):
    """Функция принимающая список словарей и опциональное значение для ключа
    state"""
    return [item for item in data if item.get("state") == state]


