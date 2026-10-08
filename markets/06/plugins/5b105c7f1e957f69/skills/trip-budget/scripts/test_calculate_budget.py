import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("calculate_budget.py")
SPEC = importlib.util.spec_from_file_location("calculate_budget", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class BudgetTests(unittest.TestCase):
    def test_conversion_statuses_and_eligible_contingency(self):
        result = MODULE.calculate({
            "base_currency": "USD", "travelers": 2, "target": 3000, "contingency_rate": "0.10",
            "items": [
                {"category": "lodging", "quantity": 2, "unit_cost": 500, "currency": "EUR", "fx_rate": "1.10", "fx_rate_date": "2026-09-19"},
                {"category": "flights", "quantity": 2, "unit_cost": 600, "contingency_eligible": False},
                {"category": "activities", "unit_cost": 200, "optional": True},
                {"category": "fees", "unit_cost": 50, "excluded": True},
            ],
        })
        self.assertEqual(result["subtotal"], "2300.00")
        self.assertEqual(result["contingency"], "110.00")
        self.assertEqual(result["status_totals"]["optional"], "200.00")
        self.assertEqual(result["target_status"], "under_target")

    def test_missing_target_is_null(self):
        result = MODULE.calculate({"travelers": 1, "items": [{"unit_cost": 10}]})
        self.assertIsNone(result["target"])
        self.assertEqual(result["target_status"], "target_not_provided")

    def test_mixed_currency_requires_dated_rate(self):
        with self.assertRaises(ValueError):
            MODULE.calculate({"base_currency": "USD", "items": [{"unit_cost": 10, "currency": "EUR"}]})

    def test_negative_cost_rejected(self):
        with self.assertRaises(ValueError):
            MODULE.calculate({"items": [{"unit_cost": -1}]})


if __name__ == "__main__":
    unittest.main()
