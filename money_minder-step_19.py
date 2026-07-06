# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: MoneyMinder
def archive_records(db_path="data/records.json"):
    """Archive completed or old records into a separate file."""
    import json, os
    from datetime import datetime

    records = load_json(db_path)
    if not isinstance(records, list):
        return "No records found."

    today = datetime.now().date()
    archive_file = db_path.replace(".json", "_archive.json")
    archived, remaining = [], []

    for i, record in enumerate(records):
        if record.get("completed"):
            archived.append(record)
        elif isinstance(record, dict) and "date" in record:
            d = datetime.strptime(str(record["date"]), "%Y-%m-%d").date()
            age_days = (today - d).days
            if age_days > 365:
                archived.append(record)
        else:
            remaining.append(record)

    save_json(archive_file, archived)
    save_json(db_path, remaining)
    return f"Archived {len(archived)} record(s). Active records: {len(remaining)}."
