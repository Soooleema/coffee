# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: MoneyMinder
def edit_record(record_id, updates):
    if record_id not in records:
        print(f"Запись с ID {record_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if hasattr(records[record_id], key) and value is not None:
            setattr(records[record_id], key, value)
    
    save_to_file()
    print(f"Запись {record_id} успешно обновлена.")
    return True

if __name__ == "__main__":
    # Пример редактирования записи (расход)
    edit_record(105, {"amount": 25.00, "category": "Еда"})
