# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: MoneyMinder
import json
from datetime import datetime, timedelta
from pathlib import Path

# Конфигурация и точки входа
APP_NAME = "MoneyMinder"
DATA_FILE = Path("money_minder_data.json")

def load_data():
    """Загрузка данных из JSON или создание пустой структуры."""
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "transactions": [],
        "goals": [],
        "settings": {"currency": "RUB", "start_date": datetime.now().date()}
    }

def save_data(data):
    """Сохранение данных в JSON."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Демонстрационные данные для первого запуска
def init_demo_data():
    today = datetime.now().date()
    demo_transactions = [
        {"id": 1, "date": (today - timedelta(days=1)).isoformat(), "type": "income", "amount": 50000, "comment": "Зарплата"},
        {"id": 2, "date": today.isoformat(), "type": "expense", "amount": 3500, "comment": "Продукты"},
        {"id": 3, "date": (today - timedelta(days=2)).isoformat(), "type": "expense", "amount": 1200, "comment": "Интернет"},
    ]
    demo_goals = [
        {"id": 1, "name": "Новый ноутбук", "target_amount": 60000, "current_amount": 0, "deadline": (today + timedelta(days=90)).isoformat()}
    ]
    
    # Инициализация и сохранение демо-данных
    data = load_data()
    data["transactions"].extend(demo_transactions)
    data["goals"].extend(demo_goals)
    save_data(data)
    print(f"Инициализация {APP_NAME} завершена. Демо-данные загружены.")

# Точка входа
if __name__ == "__main__":
    init_demo_data()
