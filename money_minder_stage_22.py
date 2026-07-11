# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: MoneyMinder
def check_overdue_reminders(reminders):
    now = datetime.now()
    overdue = [r for r in reminders if r["date"] < now and not r.get("done")]
    return overdue
