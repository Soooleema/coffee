# === Stage 45: Добавь восстановление из резервной копии ===
# Project: MoneyMinder
import json, os

def load_backup(file_path):
    if not os.path.exists(file_path):
        print(f"Резервная копия не найдена: {file_path}")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Ошибка загрузки резервной копии: {e}")
        return None

def save_backup(data, file_path):
    os.makedirs(os.path.dirname(file_path) or '.', exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Резервная копия сохранена: {file_path}")

def restore_from_backup(backup_path, data):
    if data is None:
        return False
    print("Восстановление из резервной копии...")
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Восстановлено из: {backup_path}")
    return True

def get_backup_candidates(data):
    candidates = []
    for key in data:
        if isinstance(data[key], dict) and 'backup' in data[key]:
            candidates.append((key, data[key]['backup'], data[key].get('last_modified', None)))
    candidates.sort(key=lambda x: x[2] or '', reverse=True)
    return candidates
