# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: MoneyMinder
class MoneyMinder:
    def __init__(self):
        self.records = []
        self.goals = {}

    def add_record(self, date, description, amount, category='other'):
        record = {
            'date': date,
            'description': description,
            'amount': amount,
            'category': category
        }
        self.records.append(record)
        return record

    def add_goal(self, name, target_amount, current_amount=0):
        self.goals[name] = {
            'target_amount': target_amount,
            'current_amount': current_amount
        }
        return self.goals[name]

    def get_balance(self):
        income = sum(r['amount'] for r in self.records if r['category'] == 'income')
        expense = sum(r['amount'] for r in self.records if r['category'] == 'expense')
        return income - expense

    def get_goal_progress(self, name):
        if name not in self.goals:
            return None
        goal = self.goals[name]
        progress = (goal['current_amount'] / goal['target_amount']) * 100
        return {
            'name': name,
            'current': goal['current_amount'],
            'target': goal['target_amount'],
            'progress_percent': round(progress, 2)
        }
