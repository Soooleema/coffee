# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: MoneyMinder
import json, os

DATA_FILE = "money_minder_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"transactions": [], "goals": []}
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {"transactions": [], "goals": []}

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE) or '.', exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
