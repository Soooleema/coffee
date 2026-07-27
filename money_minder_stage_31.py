# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: MoneyMinder
def switch_profile():
    profiles = list(db.profiles())
    if not profiles:
        print("Создайте профиль через /profile/create")
        return
    current_id = db.current_user_id()
    print(f"Текущий профиль: {current_id or 'не выбран'}")
    for i, p in enumerate(profiles):
        marker = " *" if (p.id == current_id) else ""
        print(f"{i+1}. {p.name}{marker}")
    choice = input("Выберите номер профиля (или 0 для сброса): ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(profiles):
            db.set_current_user_id(profiles[idx].id)
            print(f"Переключено на профиль: {profiles[idx].name}")
            return
        elif choice == "0":
            db.set_current_user_id(None)
            print("Профиль сброшен")
    except ValueError:
        pass
