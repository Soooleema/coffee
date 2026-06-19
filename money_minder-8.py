# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: MoneyMinder
def run_cli_menu():
    while True:
        print("\n=== MoneyMinder CLI ===")
        print("1. Добавить доход")
        print("2. Добавить расход")
        print("3. Просмотреть баланс")
        print("4. Выход")
        choice = input("Выберите действие (1-4): ")
        
        if choice == "1":
            amount = float(input("Сумма: "))
            desc = input("Описание: ")
            transactions.append({"type": "income", "amount": amount, "desc": desc})
            print(f"Доход {amount} добавлен.")
        elif choice == "2":
            amount = float(input("Сумма: "))
            desc = input("Описание: ")
            transactions.append({"type": "expense", "amount": amount, "desc": desc})
            print(f"Расход {amount} добавлен.")
        elif choice == "3":
            balance = sum(t["amount"] for t in transactions if t["type"] == "income") - \
                     sum(t["amount"] for t in transactions if t["type"] == "expense")
            print(f"Текущий баланс: {balance:.2f}")
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.")
