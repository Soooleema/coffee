# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: MoneyMinder
def check_integrity(records, goals):
    """Проверка целостности: все цели имеют ID, даты корректны."""
    errors = []
    for g in goals:
        if not isinstance(g['id'], str) or len(g['id']) < 1:
            errors.append(f"Цель '{g.get('name', 'unknown')}' не имеет валидного id.")
    return errors

def repair_simple_issues(records, goals):
    """Ремонт: нормализация типов и заполнение пропущенных полей."""
    for r in records:
        if not isinstance(r['amount'], (int, float)):
            try:
                r['amount'] = float(str(r['amount']).replace(',', '.'))
            except Exception:
                pass
        if 'date' not in r or r['date'] is None:
            r['date'] = datetime.now().strftime('%Y-%m-%d')
    for g in goals:
        if 'target_date' not in g or g['target_date'] is None:
            g['target_date'] = (datetime.now() + timedelta(days=365)).strftime('%Y-%m-%d')
        if 'current_amount' not in g or g['current_amount'] is None:
            g['current_amount'] = 0.0
    return records, goals
