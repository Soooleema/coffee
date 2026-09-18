# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: MoneyMinder
def export_report(report: dict) -> str:
    """Export a concise financial report to a text string."""
    lines = []
    lines.append("=== MoneyMinder Report ===")
    lines.append(f"Period: {report['period_start']} to {report['period_end']}")
    lines.append(f"Total income: {report['total_income']:.2f}")
    lines.append(f"Total expenses: {report['total_expenses']:.2f}")
    lines.append(f"Savings rate: {report.get('savings_rate', 0):.1f}%")
    lines.append(f"Goals progress: {', '.join(report.get('goals_progress', []))}")
    lines.append(f"Notes: {report.get('notes', 'None')}")
    return "\n".join(lines)
