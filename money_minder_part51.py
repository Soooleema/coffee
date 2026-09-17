# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: MoneyMinder
import time
from datetime import datetime

class Journal:
    """Журнал изменений данных с отметками времени."""

    def __init__(self):
        self.entries = []

    def log(self, message, category=None):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "category": category,
        }
        self.entries.append(entry)

    def get_entries(self):
        return self.entries

    def get_entries_by_category(self, category):
        return [e for e in self.entries if e["category"] == category]

    def get_entries_by_date(self, start_date, end_date):
        return [e for e in self.entries if start_date <= e["timestamp"] <= end_date]

    def get_entries_by_date_range(self, start_date, end_date):
        return [e for e in self.entries if start_date <= e["timestamp"] <= end_date]

    def get_entries_by_date(self, start_date, end_date):
        return [e for e in self.entries if start_date <= e["timestamp"] <= end_date]

    def get_entries_by_date_range(self, start_date, end_date):
        return [e for e in self.entries if start_date <= e["timestamp"] <= end_date]

    def get_entries_by_date(self, start_date, end_date):
        return [e for e in self.entries if start_date <= e["timestamp"] <= end_date]

    def get_entries_by_date_range(self, start_date, end_date):
        return [e for e in self.entries if start_date <= e["timestamp"] <= end_date]
