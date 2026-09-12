# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: MoneyMinder
def demo():
    print("=" * 50)
    print("  MoneyMinder — Демо сценарий")
    print("=" * 50)

    # --- 1. Создаём сберегательный аккаунт для цели "Новый ноутбук" ---
    goal = SavingsAccount("Новый ноутбук", target=50000, currency="RUB")

    # --- 2. Добавляем доходы и расходы ---
    income = Income("Зарплата", 75000, "RUB")
    expense = Expense("Супермаркет", 3500, "RUB")
    expense = Expense("Кино", 800, "RUB")
    expense = Expense("Такси", 450, "RUB")

    income.save()
    expense.save()
    expense.save()
    expense.save()

    # --- 3. Переводим часть зарплаты на цель ---
    transfer = Transfer(
        from_account="Main",
        to_account="Savings",
        amount=15000,
        description="Перевод на цель: ноутбук",
        currency="RUB"
    )
    transfer.save()

    # --- 4. Показываем отчёты ---
    print(f"\n📊 Отчёт за период: {get_current_period()}\n")

    total_income = sum(r.amount for r in Income.get_all())
    total_expense = sum(e.amount for e in Expense.get_all())
    print(f"  Доходы:   {total_income:,.0f} {Income.get_first().currency}")
    print(f"  Расходы:  {total_expense:,.0f} {Expense.get_first().currency}")
    print(f"  Баланс:   {total_income - total_expense:,.0f}")

    print(f"\n  🎯 Цель 'Новый ноутбук':")
    print(f"    Процент выполнения: {goal.percentage():.1f}%")
    print(f"    Осталось:           {goal.remaining():,.0f} {goal.currency}")

    print(f"\n  💰 Аккаунт 'Savings':")
    print(f"    Баланс: {goal.balance:,.0f} {goal.currency}")

    print(f"\n  📅 Последние 3 транзакции:")
    for t in Transaction.get_all()[-3:]:
        print(f"    {t.description:30s} {t.amount:>+,.0f} {t.currency}")

    print("\n✅ Демо завершён. Спасибо за использование MoneyMinder!")
