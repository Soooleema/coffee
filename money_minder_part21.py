# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: MoneyMinder
class Reminder:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
    
    @property
    def is_due(self):
        return datetime.date.today() >= self.due_date
    
    def __str__(self):
        status = "due" if self.is_due else f"not due until {self.due_date}"
        return f"[{status}] {self.title} (by {self.due_date})"

def add_reminders(data, reminders=None):
    data["reminders"] = reminders or []
    return data

def get_due_reminders(reminders):
    if not reminders:
        return []
    return [r for r in reminders if r.is_due]
