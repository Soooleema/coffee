# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: MoneyMinder
def main():
    import random, sys
    from datetime import date, timedelta
    categories = ['Еда', 'Транспорт', 'Развлечения', 'Жильё', 'Здоровье', 'Обучение']
    names = {
        'Доход': ['Зарплата', 'Фриланс', 'Подработка', 'Инвестиции'],
        'Расход': ['Ресторан', 'Такси', 'Кино', 'Аренда', 'Лекарства', 'Курс Python']
    }
    balances = {'Доходы': 0, 'Расходы': 0}

    print("=== Демо-режим MoneyMinder ===")
    for _ in range(15):
        kind = random.choice(['income', 'expense'])
        cat = random.choice(categories) if kind == 'expense' else random.choice(list(names['Доход']))
        name = random.choice(names.get(cat, names['Доход']))
        amount = round(random.uniform(200, 5000), 2)

        if kind == 'income':
            balances['Доходы'] += amount
            print(f"✅ ДОХОД: {name} — +{amount}")
        else:
            balances['Расходы'] += amount
            print(f"❌ РАСХОД: {cat} ({name}) — -{amount}")

    print("\n--- Итоги ---")
    print(f"Общий доход:   {balances['Доходы']:,.2f} руб.")
    print(f"Общие расходы: {balances['Расходы']:,.2f} руб.")
    net = balances['Доходы'] - balances['Расходы']
    print(f"Сальдо:        {net:+,.2f} руб.")

    if not sys.stdout.isatty():
        print("\n[Демо завершён. Данные не сохранялись.]")

if __name__ == '__main__':
    main()
