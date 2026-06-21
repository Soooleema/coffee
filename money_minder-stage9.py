# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: MoneyMinder
import json, os

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект.")
        
        # Валидация обязательных полей
        required_keys = ["income", "expense", "goal"]
        for key in required_keys:
            if key not in data:
                raise KeyError(f"Отсутствует ключ: {key}")
            
            if not isinstance(data[key], list):
                raise TypeError(f"Поле '{key}' должно быть списком.")
        
        # Преобразование строк дат в объекты datetime для удобства работы
        from datetime import datetime
        
        def parse_date(date_str):
            try:
                return datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                raise ValueError(f"Неверный формат даты: {date_str}")

        # Обогащаем данные парсингом дат и базовыми метаданными
        enriched_data = {
            "metadata": data.get("metadata", {"version": 1, "created_at": datetime.now().isoformat()}),
            "income": [{"id": i+1, **item} for i, item in enumerate(data["income"])],
            "expense": [{"id": i+1, **item} for i, item in enumerate(data["expense"])],
            "goal": data.get("goal", [])
        }

        # Обновляем даты в транзакциях
        for transaction_list in ["income", "expense"]:
            for tx in enriched_data[transaction_list]:
                if "date" in tx:
                    try:
                        tx["parsed_date"] = parse_date(tx["date"])
                    except ValueError as e:
                        print(f"Предупреждение: {e}. Дата в транзакции '{tx.get('id')}' оставлена как строка.")

        return enriched_data

    except json.JSONDecodeError as e:
        raise RuntimeError("Ошибка парсинга JSON:") from e
