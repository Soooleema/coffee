# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: MoneyMinder
def calculate_monthly_stats(transactions, goals):
    from datetime import date
    if not transactions: return {}
    stats = {}
    for t in sorted(transactions, key=lambda x: x['date'], reverse=True)[:12]:
        month_key = f"{t['date'].year}-{t['date'].month:02d}"
        if month_key not in stats:
            stats[month_key] = {'income': 0, 'expense': 0, 'balance_change': 0}
        amount = t['amount']
        is_income = t.get('type') == 'income' or (t.get('category', '').startswith(('salary', 'bonus')))
        if is_income: stats[month_key]['income'] += amount
        else: stats[month_key]['expense'] += amount
        stats[month_key]['balance_change'] = amount * (1 if is_income else -1)
    for month, data in sorted(stats.items()):
        data['net_flow'] = data['income'] - data['expense']
        data['total_volume'] = data['income'] + data['expense']
        # Простая оценка прогресса по целям для этого месяца (условно 50% от суммы целей)
        target_sum = sum(g['target_amount'] for g in goals if g.get('deadline', date.today()) > date.fromisoformat(month.replace('-', '')))
        data['goal_progress_ratio'] = min(1.0, (data['income'] - data['expense']) / max(target_sum, 1))
    return stats
