# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: MoneyMinder
def dry_run(operation, **kwargs):
    """Simulate a write operation without persisting to disk."""
    return {
        "status": "dry-run",
        "operation": operation,
        "kwargs": kwargs,
        "message": f"{operation} simulated successfully (no persistence)",
    }


def run_in_dry_mode(func, *args, **kwargs):
    """Execute a function in dry-run mode if enabled, otherwise run normally."""
    if _dry_run_enabled:
        return dry_run(func.__name__, *args, **kwargs)
    return func(*args, **kwargs)
