# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: MoneyMinder
def get_next_action(state):
    """Возвращает рекомендацию следующего действия на основе текущего состояния."""
    if state.get("balance", 0) < -500:
        return "Критический уровень долга — немедленно сократите расходы или найдите источник дохода."
    expenses = sum(x for x in state.get("expenses", []))
    income = sum(x for x in state.get("income", []))
    goals = state.get("goals", [])
    if not goals and expenses > 0:
        return "У вас нет финансовых целей — добавьте хотя бы одну сберегательную цель."
    if not income and expenses > 0:
        return "Вы не зафиксировали доходы — добавьте запись о зарплате или другом доходе."
    if state.get("last_review_date") is None or (state["today"] - state["last_review_date"]).days > 30:
        return "Пора провести финансовый обзор за последние 30 дней и обновить данные."
    if expenses > income * 0.8:
        return "Расходы составляют более 80% дохода — рассмотрите бюджетирование или сокращение трат."
    savings_rate = (income - expenses) / max(income, 1)
    if savings_rate < 0.1 and goals:
        return "Вы откладываете менее 10% дохода — увеличьте сбережения для достижения целей."
    if state.get("last_action_date") is None or (state["today"] - state["last_action_date"]).days > 7:
        return "Давно не добавляли записи — зафиксируйте хотя бы одну операцию за эту неделю."
    return "Финансы в порядке. Продолжайте вести журнал и отслеживать цели."
