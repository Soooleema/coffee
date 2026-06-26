# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: MoneyMinder
class SearchFilter:
    def __init__(self, records):
        self.records = records
    
    def search(self, query=None, category=None, date_from=None, date_to=None):
        if not isinstance(query, str) or not isinstance(category, type(None)) and not isinstance(category, str):
            raise ValueError("Invalid search parameters")
        
        results = []
        for record in self.records:
            match = True
            
            if query is not None:
                q_lower = query.lower()
                desc_match = q_lower in record.get('description', '').lower() or \
                            q_lower in str(record.get('category', '')).lower() or \
                            q_lower in str(record.get('amount', 0)).replace('-', '').lower()
                if not desc_match:
                    match = False
            
            if category is not None and record.get('category') != category:
                match = False
            
            if date_from is not None:
                rec_date = record.get('date', '')
                if isinstance(rec_date, str) and len(rec_date) >= 10:
                    try:
                        check_date = datetime.strptime(rec_date[:10], '%Y-%m-%d')
                        from_date = datetime.strptime(date_from, '%Y-%m-%d')
                        if check_date < from_date:
                            match = False
                    except ValueError:
                        pass
            
            if date_to is not None and match:
                rec_date = record.get('date', '')
                if isinstance(rec_date, str) and len(rec_date) >= 10:
                    try:
                        check_date = datetime.strptime(rec_date[:10], '%Y-%m-%d')
                        to_date = datetime.strptime(date_to, '%Y-%m-%d')
                        if check_date > to_date:
                            match = False
                    except ValueError:
                        pass
            
            if match:
                results.append(record)
        
        return results
