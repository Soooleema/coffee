# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: MoneyMinder
def undo_last_action():
    """Откат последнего действия: удаляет последнюю запись из списка операций."""
    if not last_action:
        print("Нет отменяемых действий.")
        return None
    removed = last_action.pop()
    if removed is not None and removed["type"] == "operation":
        operations.remove(removed)
    print(f"Отменено действие: {last_action[-1] if last_action else 'неизвестное'}")
    return removed
