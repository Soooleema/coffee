# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: MoneyMinder
def format_summary_report(total_income, total_expense, savings_goal, current_savings):
    """Формирует отчёт по финансовому году."""
    balance = total_income - total_expense
    progress = (current_savings / savings_goal * 100) if savings_goal else 0
    lines = [
        f"=== Отчёт за год ===",
        f"Доход: {total_income:,.2f}",
        f"Расход: {total_expense:,.2f}",
        f"Баланс: {balance:,.2f}",
        f"Накопления: {current_savings:,.2f}",
        f"Цель: {savings_goal:,.2f}",
        f"Прогресс: {progress:.1f}%",
        f"================================",
    ]
    return "\n".join(lines)
