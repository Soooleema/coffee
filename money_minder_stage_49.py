# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: MoneyMinder
def main():
    print("=== MoneyMinder — Самопроверка ===")
    print(f"Список категорий: {list(CATEGORIES.keys())}")
    print(f"Список целей: {list(GOALS.keys())}")
    print(f"Список пользователей: {list(USERS.keys())}")
    print(f"Сумма всех доходов: {sum(TotalIncome.values()):.2f}")
    print(f"Сумма всех расходов: {sum(TotalExpenses.values()):.2f}")
    print(f"Сальдо: {sum(TotalIncome.values()) - sum(TotalExpenses.values()):.2f}")
    print(f"Список целей: {list(GOALS.items())}")
    print(f"Список пользователей: {list(USERS.items())}")
    print(f"Список категорий: {list(CATEGORIES.items())}")

main()
