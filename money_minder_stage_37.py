# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: MoneyMinder
import unittest
from datetime import date

class TestMoneyMinder(unittest.TestCase):
    def test_add_income(self):
        from money.mind import Mind
        m = Mind()
        m.add_income(1000, "Salary", date(2024, 1, 1))
        self.assertEqual(len(m.incomes), 1)
        self.assertEqual(m.incomes[0].amount, 1000)

    def test_add_expense(self):
        from money.mind import Mind
        m = Mind()
        m.add_expense(500, "Coffee", date(2024, 1, 1))
        self.assertEqual(len(m.expenses), 1)
        self.assertEqual(m.expenses[0].amount, 500)

    def test_add_savings_goal(self):
        from money.mind import Mind
        m = Mind()
        m.add_savings_goal(5000, "Vacation", date(2024, 6, 1))
        self.assertEqual(len(m.goals), 1)
        self.assertEqual(m.goals[0].amount, 5000)

    def test_add_report(self):
        from money.mind import Mind
        m = Mind()
        m.add_income(2000, "Salary", date(2024, 1, 1))
        m.add_expense(800, "Rent", date(2024, 1, 1))
        report = m.make_report(date(2024, 1, 1), date(2024, 1, 31))
        self.assertEqual(report.total_income, 2000)
        self.assertEqual(report.total_expense, 800)

    def test_make_report_empty(self):
        from money.mind import Mind
        m = Mind()
        report = m.make_report(date(2024, 1, 1), date(2024, 1, 31))
        self.assertEqual(report.total_income, 0)
        self.assertEqual(report.total_expense, 0)

    def test_make_report_invalid_dates(self):
        from money.mind import Mind
        m = Mind()
        with self.assertRaises(ValueError):
            m.make_report(date(2024, 1, 31), date(2024, 1, 1))

    def test_make_report_date_equal(self):
        from money.mind import Mind
        m = Mind()
        report = m.make_report(date(2024, 1, 1), date(2024, 1, 1))
        self.assertEqual(report.total_income, 0)
        self.assertEqual(report.total_expense, 0)

if __name__ == "__main__":
    unittest.main()
