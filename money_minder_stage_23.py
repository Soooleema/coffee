# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: MoneyMinder
def print_table(title, headers, rows):
    """Compact console table formatter."""
    widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if len(str(cell)) > widths[i]:
                widths[i] = len(str(cell))
    line = "".join("-" * w for w in widths) + "+"
    print(f"\n{title}\n{line}")
    print("| " + "| ".join(str(h).ljust(widths[i]) for i, h in enumerate(headers)) + " |")
    print(line)
    for row in rows:
        print("| " + "| ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(row)) + " |")
    print(line)
