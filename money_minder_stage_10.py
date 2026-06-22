# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: MoneyMinder
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "timestamp": datetime.now().isoformat(),
        "income_records": income_records,
        "expense_records": expense_records,
        "savings_goals": savings_goals,
        "reports": reports
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
