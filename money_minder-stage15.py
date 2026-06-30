# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: MoneyMinder
def get_weekly_statistics(records):
    from datetime import date, timedelta
    
    if not records:
        return []
    
    grouped = {}
    for r in records:
        d = date.fromisoformat(r['date'])
        week_start = (d - timedelta(days=d.weekday())).isoformat()
        key = f"{week_start}+{r.get('category', 'other')}"
        
        if key not in grouped:
            grouped[key] = {'income': 0, 'expense': 0, 'count': 0}
        
        amount = r['amount']
        if r['type'] == 'income':
            grouped[key]['income'] += amount
        else:
            grouped[key]['expense'] += amount
        
        grouped[key]['count'] += 1
    
    result = []
    for key, stats in sorted(grouped.items()):
        week_start_str, category = key.split('+', 1)
        start_date = date.fromisoformat(week_start_str)
        
        # Calculate end date of the week (Sunday)
        days_in_week = [start_date + timedelta(days=i) for i in range(7)]
        
        result.append({
            'category': category,
            'start_date': start_date.isoformat(),
            'end_date': days_in_week[6].isoformat(),
            'income': stats['income'],
            'expense': stats['expense'],
            'balance': stats['income'] - stats['expense'],
            'transaction_count': stats['count']
        })
    
    return result
