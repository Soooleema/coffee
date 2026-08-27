# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: MoneyMinder
import unittest

class TestEdgeCases(unittest.TestCase):
    def test_empty_transactions(self):
        journal = Journal()
        report = journal.get_report()
        self.assertEqual(report["summary"]["total_income"], 0)
        self.assertEqual(report["summary"]["total_expense"], 0)

    def test_negative_amount_rejected(self):
        journal = Journal()
        with self.assertRaises(ValueError):
            journal.add_transaction("income", -100, "test")
        with self.assertRaises(ValueError):
            journal.add_transaction("expense", -50, "test")

    def test_invalid_category(self):
        journal = Journal()
        with self.assertRaises(ValueError):
            journal.add_transaction("income", 100, "invalid_cat")

    def test_goal_amount_zero(self):
        journal = Journal()
        goal = Goal("test_goal", 0, 0.0)
        self.assertTrue(goal.is_reached())
        self.assertEqual(goal.progress(), 1.0)

    def test_goal_negative_amount(self):
        journal = Journal()
        goal = Goal("test_goal", -100, 0.0)
        self.assertTrue(goal.is_reached())

    def test_goal_progress_over_100(self):
        journal = Journal()
        goal = Goal("test_goal", 1000, 1500.0)
        self.assertTrue(goal.is_reached())
        self.assertEqual(goal.progress(), 1.5)

    def test_goal_progress_under_0(self):
        journal = Journal()
        goal = Goal("test_goal", 1000, -100.0)
        self.assertFalse(goal.is_reached())
        self.assertEqual(goal.progress(), -0.1)

    def test_goal_invalid_progress(self):
        journal = Journal()
        with self.assertRaises(ValueError):
            Goal("test_goal", 1000, 1000.0, 0.5)
        with self.assertRaises(ValueError):
            Goal("test_goal", 1000, 1000.0, -1.0)
        with self.assertRaises(ValueError):
            Goal("test_goal", 1000, 1000.0, 1.5)

    def test_goal_name_empty(self):
        journal = Journal()
        with self.assertRaises(ValueError):
            Goal("", 1000, 0.0)

    def test_goal_amount_empty(self):
        journal = Journal()
        with self.assertRaises(ValueError):
            Goal("test_goal", "", 0.0)

    def test_goal_progress_empty(self):
        journal = Journal()
        with self.assertRaises(ValueError):
            Goal("test_goal", 1000, "")

    def test_goal_amount_negative(self):
        journal = Journal()
        with self.assertRaises(ValueError):
            Goal("test_goal", -1000, 0.0)

    def test_goal_progress_negative(self):
        journal = Journal()
        with self.assertRaises(ValueError):
            Goal("test_goal", 1000, -100.0)

    def test_goal_progress_over_100(self):
        journal = Journal()
        with self.assertRaises(ValueError):
            Goal("test_goal", 1000, 1500.0)

if __name__ == "__main__":
    unittest.main()
