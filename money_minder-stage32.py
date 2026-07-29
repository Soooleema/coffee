# === Stage 32: Добавь журнал действий пользователя ===
# Project: MoneyMinder
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, action_type, description, amount=None):
        entry = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'action_type': action_type,
            'description': description,
            'amount': amount
        }
        self.entries.append(entry)

    def get_summary(self):
        return '\n'.join(
            f"[{e['timestamp']}] {e['action_type'].upper()}: {e['description']}" + (f" ({e['amount']})" if e.get('amount') else '')
            for e in self.entries
        )

    def clear(self):
        self.entries.clear()
