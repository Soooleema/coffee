# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: MoneyMinder
def delete_record(record_id: int, record_type: str) -> bool:
    if not isinstance(record_id, int) or record_id <= 0:
        raise ValueError("ID должен быть положительным целым числом")
    
    try:
        with open('money_minder_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, dict):
            return False
            
        records_to_delete = []
        for key in list(data.keys()):
            record = data[key]
            if (record.get('id') == record_id and 
                record.get('type') == record_type and 
                record.get('deleted', False) != True):
                
                # Помечаем запись как удаленную, а не удаляем из словаря сразу
                # чтобы сохранить структуру и возможность восстановления при необходимости
                record['deleted'] = True
                records_to_delete.append(key)
        
        if not records_to_delete:
            return False
            
        with open('money_minder_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"Удалено {len(records_to_delete)} записей(ей) типа '{record_type}'")
        return True
        
    except (FileNotFoundError, PermissionError):
        print("Ошибка доступа к файлу данных или файл не найден.")
        return False
