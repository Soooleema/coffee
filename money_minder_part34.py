# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: MoneyMinder
TEMPLATES = {
    "coffee": {"category": "food", "amount": 350, "note": "Кофе в кафе"},
    "bus_pass": {"category": "transport", "amount": -1200, "note": "Подписка на автобус"},
    "salary_monthly": {"category": "income", "amount": 80000, "note": "Зарплата за месяц"},
    "groceries_weekly": {"category": "food", "amount": -2500, "note": "Продукты на неделю"},
}

def apply_template(name):
    if name not in TEMPLATES:
        print(f"Неизвестный шаблон: {name}")
        return None
    t = TEMPLATES[name].copy()
    amount_str = input(f"Сумма шаблона '{name}' ({t['amount']} руб)? ").strip()
    if not amount_str:
        t["amount"] *= 1.0
    else:
        try:
            t["amount"] = float(amount_str)
        except ValueError:
            print("Неверный формат суммы")
            return None
    t["note"] = input(f"Примечание к записи? ").strip() or t.get("note", "")
    t["date"] = datetime.date.today().isoformat()
    record = Record(**t)
    if not record.validate():
        print("Запись невалидна")
        return None
    records.append(record)
    print(f"Добавлена запись по шаблону '{name}'")
    return record
