# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: MoneyMinder
def backup_data(file_path: str, backup_dir: str = "backups") -> str:
    """Создаёт резервную копию файла данных с таймстампом."""
    from datetime import datetime
    import shutil
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}_{os.path.basename(file_path)}")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл данных не найден: {file_path}")
    shutil.copy2(file_path, backup_path)
    return backup_path
