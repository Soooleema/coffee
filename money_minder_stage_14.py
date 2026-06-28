# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: MoneyMinder
def generate_summary(transactions, goals):
    income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = income - expense
    savings_rate = (1 - expense / income) * 100 if income > 0 else 0
    total_goal_progress = sum(g['current'] / g['target'] * 100 for g in goals.values()) if goals else 0
    print(f"=== Сводка MoneyMinder ===")
    print(f"Доходы: {income:.2f} | Расходы: {expense:.2f} | Баланс: {balance:.2f}")
    print(f"Процент сбережений: {savings_rate:.1f}%")
    if goals:
        print("Прогресс по целям:")
        for name, data in sorted(goals.items(), key=lambda x: x[0]):
            pct = (data['current'] / data['target']) * 100
            print(f"  {name}: {pct:.1f}% ({data['current']} из {data['target']})")
    else:
        print("Активные цели отсутствуют.")
