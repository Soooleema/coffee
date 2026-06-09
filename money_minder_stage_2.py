# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: MoneyMinder
class MoneyModel:
    def __init__(self):
        self.incomes = []
        self.expenses = []
        self.goals = []

    def validate_amount(self, amount):
        try:
            return float(amount) > 0
        except ValueError:
            return False

    def validate_date(self, date_str):
        import datetime
        try:
            if 'T' in date_str:
                dt = datetime.datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            else:
                dt = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def add_income(self, description, amount, date):
        if not self.validate_amount(amount) or not self.validate_date(date):
            return False
        self.incomes.append({'description': description, 'amount': float(amount), 'date': date})
        return True

    def add_expense(self, description, amount, date):
        if not self.validate_amount(amount) or not self.validate_date(date):
            return False
        self.expenses.append({'description': description, 'amount': float(amount), 'date': date})
        return True

    def add_goal(self, name, target_amount, deadline):
        if not self.validate_amount(target_amount) or not self.validate_date(deadline):
            return False
        self.goals.append({'name': name, 'target_amount': float(target_amount), 'deadline': deadline})
        return True
