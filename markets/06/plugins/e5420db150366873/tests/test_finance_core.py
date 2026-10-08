from __future__ import annotations
import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import finance_core as f


class AccountingTests(unittest.TestCase):
    def test_three_statement_pass_and_fail(self):
        self.assertTrue(f.three_statement_reconcile(100, 60, 40, 10, 14, 8, -3, -1)["pass"])
        self.assertFalse(f.three_statement_reconcile(101, 60, 40, 10, 14, 8, -3, -1)["pass"])

    def test_cash_flow_reconcile(self):
        self.assertTrue(f.cash_flow_reconcile(10, 3, 2, 1, 12)["pass"])

    def test_share_bridge(self):
        result = f.share_count_bridge(100, sbc_issuance=4, repurchases=3, ending_shares=101)
        self.assertTrue(result["pass"])
        self.assertEqual(result["gross_dilution"], 4)

    def test_working_capital(self):
        result = f.working_capital_metrics(100, 50, 30, 1000, 600)
        self.assertAlmostEqual(result["cash_conversion_cycle"], result["dso"] + result["dio"] - result["dpo"])

    def test_lease(self):
        result = f.lease_normalization(20, 4, 100, 80, 200)
        self.assertEqual(result["lease_adjusted_ebitda"], 100)
        self.assertEqual(result["lease_adjusted_debt"], 300)

    def test_sbc(self):
        result = f.sbc_dilution(100, 102, 3, 10, 200, 25)
        self.assertEqual(result["gross_issuance_estimate"], 5)

    def test_tax(self):
        result = f.tax_normalization(100, 30, discrete_items=5, statutory_rate=.21)
        self.assertAlmostEqual(result["normalized_effective_rate"], .25)


class ValuationTests(unittest.TestCase):
    def test_dcf(self):
        result = f.dcf([100, 110, 121], .10, .03, net_debt=50, diluted_shares=10)
        self.assertAlmostEqual(result["value_per_share"], (result["enterprise_value"] - 50) / 10)

    def test_dcf_rejects_bad_terminal(self):
        with self.assertRaises(ValueError):
            f.dcf([100], .03, .03)

    def test_reverse_dcf(self):
        target = f.dcf([110, 121, 133.1], .10, .03)["enterprise_value"]
        result = f.reverse_dcf_implied_growth(target, 100, 3, .10, .03)
        self.assertAlmostEqual(result["implied_growth"], .10, places=7)

    def test_multiples(self):
        result = f.multiples_valuation(100, 8, net_debt=200, diluted_shares=20)
        self.assertEqual(result["value_per_share"], 30)

    def test_sotp(self):
        result = f.sum_of_parts([{"name": "A", "metric": 10, "multiple": 5}, {"name": "B", "metric": 20, "multiple": 3}], net_debt=10)
        self.assertEqual(result["equity_value"], 100)

    def test_residual_income(self):
        result = f.residual_income(100, [.15, .15], .10, payout_ratio=.5)
        self.assertGreater(result["equity_value"], 100)

    def test_scenario(self):
        result = f.scenario_valuation([50, 100, 200], [.2, .5, .3])
        self.assertEqual(result["expected_value"], 120)
        with self.assertRaises(ValueError):
            f.scenario_valuation([1, 2], [.4, .4])


class ForensicAndRiskTests(unittest.TestCase):
    def test_accruals(self):
        self.assertEqual(f.accruals(100, 80, 1000)["accrual_ratio"], .02)

    def test_beneish(self):
        result = f.beneish_m_score(1, 1, 1, 1, 1, 1, 1, 0)
        self.assertIn("diagnostic", result["interpretation"])

    def test_cash_conversion(self):
        self.assertEqual(f.cash_conversion(100, 120)["cfo_to_net_income"], 1.2)

    def test_wc_anomaly(self):
        result = f.working_capital_anomalies(.05, .20, .04, .03)
        self.assertIn("receivables_vs_revenue", result["flags"])

    def test_disclosure_drift(self):
        result = f.disclosure_drift("stable demand and margins", "weak demand and lower margins")
        self.assertTrue(result["material_review_required"])

    def test_liquidity(self):
        self.assertEqual(f.liquidity_runway(100, 50, 10, 20, 10)["runway_periods"], 12)

    def test_debt_maturity(self):
        result = f.debt_maturity_schedule({"2027": 100, "2028": 150}, 60, 30)
        self.assertEqual(result["total_maturities"], 250)

    def test_covenants(self):
        self.assertTrue(f.covenant_headroom(3, 4)["pass"])
        self.assertFalse(f.covenant_headroom(5, 4)["pass"])

    def test_refinancing(self):
        result = f.refinancing_stress(100, .05, .09, 40, 10)
        self.assertAlmostEqual(result["incremental_interest"], 4)

    def test_dilution(self):
        result = f.dilution_stress(100, 10, 100, discount=.2)
        self.assertAlmostEqual(result["new_shares"], 12.5)


class ResearchSystemMathTests(unittest.TestCase):
    def test_forecast_error(self):
        result = f.forecast_error(100, 110, {"volume": 4, "price": 6})
        self.assertTrue(result["pass"])

    def test_bias(self):
        result = f.forecast_bias([1, -1, 2, -2])
        self.assertEqual(result["mean_error"], 0)

    def test_management_score(self):
        result = f.management_credibility([{"outcome": "met"}, {"outcome": "missed"}, {"outcome": "not_yet_due"}])
        self.assertEqual(result["score"], 50)

    def test_confidence(self):
        components = {name: 80 for name in f.CONFIDENCE_WEIGHTS}
        self.assertEqual(f.research_confidence(components)["weighted_score"], 80)
        self.assertEqual(f.research_confidence(components, mandatory_gate_open=True)["weighted_score"], 59)

    def test_freshness(self):
        self.assertFalse(f.evidence_freshness(10, 30)["stale"])
        self.assertTrue(f.evidence_freshness(31, 30)["stale"])

    def test_evoi(self):
        high = f.evoi_priority(1, .8, .8, 2, 1)["priority_score"]
        low = f.evoi_priority(.2, .2, .2, 1, 4)["priority_score"]
        self.assertGreater(high, low)


class ParameterRegressionTests(unittest.TestCase):
    def test_120_deterministic_parameter_cases(self):
        for i in range(1, 41):
            with self.subTest(kind="pvm_like_working_capital", i=i):
                metrics = f.working_capital_metrics(i * 2, i, i / 2, i * 20, i * 12)
                self.assertTrue(math.isfinite(metrics["cash_conversion_cycle"]))
        for i in range(1, 41):
            with self.subTest(kind="scenario", i=i):
                values = [float(i), float(i * 2), float(i * 3)]
                self.assertAlmostEqual(f.scenario_valuation(values, [.2, .5, .3])["expected_value"], i * 2.1)
        for i in range(1, 41):
            with self.subTest(kind="freshness", i=i):
                result = f.evidence_freshness(i, 30)
                self.assertEqual(result["stale"], i > 30)


if __name__ == "__main__":
    unittest.main()
