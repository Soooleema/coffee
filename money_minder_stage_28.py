# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: MoneyMinder
import statistics

def compute_project_metrics(records, goals):
    total_income = sum(r['amount'] for r in records if r['type'] == 'income')
    total_expense = sum(r['amount'] for r in records if r['type'] == 'expense')
    savings = total_income - total_expense

    net_monthly = {}
    from collections import defaultdict
    monthly_records = defaultdict(list)
    for r in records:
        month_key = f"{r['date'][0]}-{r['date'][1]}"
        monthly_records[month_key].append(r['amount'])
    for m, amounts in monthly_records.items():
        net_monthly[m] = sum(a for a in amounts if 'income' in r.get('category', '') or True) - \
                         sum(a for a in amounts if 'expense' in r.get('category', '') or True)

    goal_progress = {}
    for g in goals:
        current = sum(r['amount'] for r in records if r.get('goal_id') == g['id'])
        goal_progress[g['name']] = {
            'target': g['target'],
            'current': current,
            'percent': (current / g['target'] * 100) if g['target'] else 0,
            'remaining': g['target'] - current,
        }

    return {
        'total_income': total_income,
        'total_expense': total_expense,
        'savings': savings,
        'average_monthly_spend': statistics.mean([sum(a) for a in monthly_records.values()]) if monthly_records else 0,
        'goal_progress': goal_progress,
    }
