# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: MoneyMinder
def reset_demo_data():
    """Сбросить демо-данные в таблицы доходов, расходов и целей."""
    for table in ['income', 'expense', 'goal']:
        cursor.execute(f"DELETE FROM {table}")
    return "Демо-данные сброшены."

def clear_state(app):
    """Очистить состояние приложения: сбросить демо-данные, очистить поля ввода и скрыть отчёты."""
    reset_demo_data()
    app['input_income'] = ''
    app['input_expense'] = ''
    app['input_goal_amount'] = ''
    app['active_tab'] = 'dashboard'
    hide_reports(app)
