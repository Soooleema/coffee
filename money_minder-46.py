# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: MoneyMinder
def migrate_to_v2(data: dict) -> dict:
    if data.get("version") != 2:
        data["version"] = 2
        if "transactions" not in data:
            data["transactions"] = []
        if "savings_goals" not in data:
            data["savings_goals"] = []
        if "reports" not in data:
            data["reports"] = []
    return data
