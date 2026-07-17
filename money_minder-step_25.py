# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: MoneyMinder
def parse_date(date_str):
    """Парсит дату в формате ДД.ММ.ГГГГ или ГГГГ-ММ-ДД. Возвращает datetime.date."""
    import datetime as dt
    if not isinstance(date_str, str) or len(date_str.strip()) == 0:
        raise ValueError("Дата пуста")
    date_str = date_str.strip()
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            return dt.datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Неверный формат даты: '{date_str}'. Ожидаем ДД.ММ.ГГГГ или ГГГГ-ММ-ДД")
