# === Stage 17: Добавь группировку записей по категориям ===
# Project: MoneyMinder
def group_by_category(records):
    from collections import defaultdict
    grouped = defaultdict(list)
    for record in records:
        cat = record.get('category', 'Other') or 'Other'
        grouped[cat].append(record)
    return dict(grouped)
