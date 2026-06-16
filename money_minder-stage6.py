# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: MoneyMinder
class Filter:
    def __init__(self, records):
        self.records = records
    
    def filter_by_status(self, status=None):
        if status is None:
            return list(self.records)
        return [r for r in self.records if r.get('status') == status]
    
    def filter_by_category(self, category=None):
        if category is None:
            return list(self.records)
        return [r for r in self.records if r.get('category') == category]
    
    def filter_by_tag(self, tag=None):
        if tag is None:
            return list(self.records)
        return [r for r in self.records if tag in r.get('tags', [])]
    
    def apply_filters(self, status=None, category=None, tags=None):
        result = self.filter_by_status(status)
        result = self.filter_by_category(category, result)
        if tags:
            result = [r for r in result if any(t in r.get('tags', []) for t in tags)]
        return result
