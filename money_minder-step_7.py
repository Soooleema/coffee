# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: MoneyMinder
def sort_transactions(transactions, key='date'):
    reverse = False if key == 'date' else True
    if key == 'name':
        return sorted(transactions, key=lambda x: (x['category'] or '').lower(), reverse=False)
    elif key == 'priority':
        priority_map = {'high': 1, 'medium': 2, 'low': 3}
        return sorted(transactions, key=lambda x: priority_map.get(x.get('priority', 'medium'), 2), reverse=True)
    else:
        return sorted(transactions, key=lambda x: x['date'], reverse=reverse)
