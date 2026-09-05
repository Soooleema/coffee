# === Stage 43: Добавь пагинацию длинных списков ===
# Project: MoneyMinder
def paginate(items, page_size=10):
    """Return (page, total_pages, total_items) for a 1-based page index."""
    total = len(items)
    total_pages = max(1, (total + page_size - 1) // page_size)
    idx = (page - 1) * page_size
    return items[idx:idx + page_size], total_pages, total
