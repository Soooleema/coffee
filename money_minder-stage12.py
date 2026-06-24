# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: MoneyMinder
def load_from_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict):
            return [data]
        elif isinstance(data, list):
            return data
        else:
            raise ValueError("Неверный формат данных JSON")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {file_path}: {e}")
        return []
