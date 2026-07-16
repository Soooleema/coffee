# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: MoneyMinder
def print_record_summary(record):
    """Print a compact one-line summary of a record followed by its details."""
    if isinstance(record, Income):
        kind = "Income"
    elif isinstance(record, Expense):
        kind = "Expense"
    elif isinstance(record, Goal):
        kind = "Goal"
    else:
        kind = type(record).__name__

    # Extract key fields based on record type
    if isinstance(record, Income):
        details = {
            'amount': f"{record.amount:.2f}",
            'category': record.category or '-',
            'date': str(record.date),
            'description': (record.description or '')[:30],
        }
    elif isinstance(record, Expense):
        details = {
            'amount': f"-{record.amount:.2f}",
            'category': record.category or '-',
            'date': str(record.date),
            'description': (record.description or '')[:30],
        }
    elif isinstance(record, Goal):
        target = record.target_amount if hasattr(record, 'target_amount') else '?'
        current = record.current_amount if hasattr(record, 'current_amount') else 0.0
        pct = (current / target * 100) if target > 0 else 0
        details = {
            'name': record.name or '-',
            'target': f"{target:.2f}",
            'current': f"{current:.2f}",
            'progress': f"{pct:.1f}%",
        }
    else:
        details = {'type': kind, 'raw': str(record)[:80]}

    # Print header line with amount/summary first
    if isinstance(record, (Income, Expense)):
        print(f"[{kind}] {record.date or '-'}  |  "
              f"Amount: {details['amount']}  |  "
              f"Category: {details['category']}")
        if details['description']:
            print(f"    Description: {details['description']}")
    elif isinstance(record, Goal):
        print(f"[{kind}] {record.name or '-'}  |  "
              f"Target: {details['target']}  |  "
              f"Current: {details['current']}  ({details['progress']})")
