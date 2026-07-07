# === Stage 20: Добавь восстановление записей из архива ===
# Project: MoneyMinder
def archive_restore(archive_path):
    """Восстановить записи из текстового архива в формат MoneyMinder."""
    with open(archive_path, 'r', encoding='utf-8') as f:
        lines = [ln.strip() for ln in f.readlines() if ln.strip()]

    records = []
    current_type = None
    current_date = None
    current_amount = 0.0
    current_note = ''
    current_category = None

    for ln in lines:
        parts = ln.split('|')
        if len(parts) >= 4:
            date_str, amount_str, note, category = [p.strip() for p in parts[:4]]
            try:
                records.append({
                    'date': date_str,
                    'amount': float(amount_str),
                    'note': note or '',
                    'category': category or 'other'
                })
            except ValueError:
                continue
    return records
