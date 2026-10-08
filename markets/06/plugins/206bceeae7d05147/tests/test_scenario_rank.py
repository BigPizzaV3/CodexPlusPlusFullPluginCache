import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest
import uuid


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "scenario_rank.py"
FIXTURE = ROOT / "tests" / "fixtures" / "scenario-example.json"
SPEC = importlib.util.spec_from_file_location("scenario_rank", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ScenarioTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_independent_arithmetic_and_annualization(self):
        result = MODULE.analyze(self.data)
        alpha = result["companies"][0]
        expected = 0.2 * 0.67 + 0.5 * 1.94 + 0.3 * 3.21
        self.assertAlmostEqual(alpha["central"]["expected_total_return"], expected - 1)
        self.assertAlmostEqual(alpha["central"]["annualized_expected_wealth"], expected ** (1 / 7) - 1)
        scenario_average = 0.2 * (0.67 ** (1 / 7) - 1) + 0.5 * (1.94 ** (1 / 7) - 1) + 0.3 * (3.21 ** (1 / 7) - 1)
        self.assertAlmostEqual(alpha["central"]["probability_weighted_scenario_cagr"], scenario_average)
        self.assertNotAlmostEqual(scenario_average, expected ** (1 / 7) - 1)
        self.assertAlmostEqual(alpha["robust_success_probability"], 0.8)
        self.assertAlmostEqual(alpha["robust_severe_loss_probability"], 0.2)
        self.assertTrue(alpha["eligible"])

    def test_total_loss_and_exact_success_boundaries(self):
        self.data["horizon_years"] = 1
        company = self.data["companies"][0]
        company["scenario_sets"] = [{"name": "central", "scenarios": [
            {"name": "loss", "probability": 0.2, "terminal_price": 0, "cash_distributions": 0, "benchmark_wealth_multiple": 0},
            {"name": "flat", "probability": 0.2, "terminal_price": 100, "cash_distributions": 0, "benchmark_wealth_multiple": 0.9},
            {"name": "tie", "probability": 0.2, "terminal_price": 150, "cash_distributions": 0, "benchmark_wealth_multiple": 1.5},
            {"name": "wins", "probability": 0.4, "terminal_price": 180, "cash_distributions": 20, "benchmark_wealth_multiple": 1.5},
        ]}]
        central = MODULE.analyze(self.data)["companies"][0]["central"]
        self.assertEqual(central["scenarios"][0]["scenario_cagr"], -1)
        self.assertEqual(central["success_probability"], 0.4)
        self.assertEqual(central["severe_loss_probability"], 0.2)

    def test_threshold_is_inclusive(self):
        row = self.data["companies"][0]["scenario_sets"][0]["scenarios"][0]
        row["terminal_price"], row["cash_distributions"] = 60, 0
        central = MODULE.analyze(self.data)["companies"][0]["central"]
        self.assertTrue(central["scenarios"][0]["severe_loss"])

    def test_decimal_loss_and_probability_boundaries(self):
        self.data["severe_loss_threshold"] = 0.1
        self.data["policy"]["max_severe_loss_probability"] = 0.3
        self.data["policy"]["min_success_probability"] = 0.7
        company = self.data["companies"][0]
        for scenario_set in company["scenario_sets"]:
            scenario_set["scenarios"] = [
                {"name": "loss-a", "probability": 0.1, "terminal_price": 90, "cash_distributions": 0, "benchmark_wealth_multiple": 1},
                {"name": "loss-b", "probability": 0.2, "terminal_price": 90, "cash_distributions": 0, "benchmark_wealth_multiple": 1},
                {"name": "gain", "probability": 0.7, "terminal_price": 200, "cash_distributions": 0, "benchmark_wealth_multiple": 1},
            ]
        company["scenario_sets"][1]["scenarios"][2]["terminal_price"] = 190
        row = MODULE.analyze(self.data)["companies"][0]
        self.assertEqual(row["robust_severe_loss_probability"], 0.3)
        self.assertTrue(row["eligible"])

    def test_all_loss_has_finite_minus_one_returns(self):
        for company in self.data["companies"]:
            for scenario_set in company["scenario_sets"]:
                for row in scenario_set["scenarios"]:
                    row["terminal_price"] = row["cash_distributions"] = 0
        result = MODULE.analyze(self.data)
        self.assertEqual(result["ranked_ids"], [])
        for row in result["companies"]:
            self.assertEqual(row["central"]["annualized_expected_wealth"], -1)
            self.assertEqual(row["central"]["probability_weighted_scenario_cagr"], -1)

    def test_central_only_and_renamed_identical_sensitivity_not_rankable(self):
        company = self.data["companies"][0]
        company["scenario_sets"] = company["scenario_sets"][:1]
        self.assertFalse(MODULE.analyze(self.data)["companies"][0]["eligible"])
        duplicate = copy.deepcopy(company["scenario_sets"][0])
        duplicate["name"] = "renamed"
        duplicate["scenarios"].reverse()
        company["scenario_sets"].append(duplicate)
        self.assertFalse(MODULE.analyze(self.data)["companies"][0]["has_distinct_sensitivity"])

    def test_optimistic_only_sensitivity_is_not_rankable(self):
        company = self.data["companies"][0]
        sensitivity = copy.deepcopy(company["scenario_sets"][0])
        sensitivity["name"] = "only_upside"
        for row in sensitivity["scenarios"]:
            row["terminal_price"] += 100
        company["scenario_sets"] = [company["scenario_sets"][0], sensitivity]
        result = MODULE.analyze(self.data)["companies"][0]
        self.assertTrue(result["has_distinct_sensitivity"])
        self.assertFalse(result["has_adverse_sensitivity"])
        self.assertFalse(result["eligible"])
        self.assertIsNone(result["rank"])

    def test_split_state_and_zero_mass_do_not_manufacture_stress(self):
        for add_zero_mass in (False, True):
            data = copy.deepcopy(self.data)
            company = data["companies"][0]
            sensitivity = copy.deepcopy(company["scenario_sets"][0])
            sensitivity["name"] = "same_distribution_split"
            original = sensitivity["scenarios"][0]
            original["probability"] /= 2
            second_half = copy.deepcopy(original)
            second_half["name"] = "other_half"
            sensitivity["scenarios"].append(second_half)
            if add_zero_mass:
                sensitivity["scenarios"].append({
                    "name": "impossible_loss", "probability": 0,
                    "terminal_price": 0, "cash_distributions": 0,
                    "benchmark_wealth_multiple": 1})
            company["scenario_sets"] = [company["scenario_sets"][0], sensitivity]
            with self.subTest(add_zero_mass=add_zero_mass):
                result = MODULE.analyze(data)["companies"][0]
                self.assertFalse(result["has_distinct_sensitivity"])
                self.assertFalse(result["has_adverse_sensitivity"])
                self.assertFalse(result["eligible"])

    def test_genuine_adverse_sensitivity_is_accepted(self):
        result = MODULE.analyze(self.data)
        for company in result["companies"]:
            self.assertTrue(company["has_adverse_sensitivity"])
            self.assertTrue(company["eligible"])

    def test_pareto_dominance_and_deterministic_ties(self):
        original = self.data["companies"][0]
        equal = copy.deepcopy(original)
        equal["id"] = "FICTION:AARDVARK"
        worse = copy.deepcopy(original)
        worse["id"] = "FICTION:WORSE"
        for scenario_set in worse["scenario_sets"]:
            scenario_set["scenarios"][2]["terminal_price"] -= 10
        self.data["companies"] = [worse, original, equal]
        result = MODULE.analyze(self.data)
        self.assertEqual(result["ranked_ids"], ["FICTION:AARDVARK", "FICTION:ALPHA", "FICTION:WORSE"])
        self.assertEqual(result["companies"][0]["dominated_by"], ["FICTION:AARDVARK", "FICTION:ALPHA"])
        self.data["companies"].reverse()
        self.assertEqual(MODULE.analyze(self.data)["ranked_ids"], result["ranked_ids"])

    def test_bad_numeric_values_and_currency(self):
        mutations = [
            lambda d: d.update(horizon_years=0),
            lambda d: d.update(horizon_years=True),
            lambda d: d.update(horizon_years=float("nan")),
            lambda d: d.update(severe_loss_threshold=0),
            lambda d: d.update(severe_loss_threshold=1.1),
            lambda d: d["policy"].update(min_success_probability=-0.01),
            lambda d: d["policy"].update(max_severe_loss_probability=2),
            lambda d: d["companies"][0].update(currency="EUR"),
            lambda d: d["companies"][0]["price"].update(value=0),
            lambda d: d["companies"][0]["price"].update(value=float("inf")),
            lambda d: d["companies"][0]["price"].update(value=10**1000),
            lambda d: d["companies"][0].update(name=" "),
            lambda d: d["companies"][0].update(evidence_eligible=1),
        ]
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                data = copy.deepcopy(self.data)
                mutation(data)
                with self.assertRaises(MODULE.ValidationError):
                    MODULE.analyze(data)

    def test_probabilities_and_wealth_inputs(self):
        for key, value in [("probability", True), ("probability", -0.2), ("probability", 0.3),
                           ("probability", float("nan")), ("terminal_price", -1),
                           ("cash_distributions", -1), ("benchmark_wealth_multiple", -1)]:
            with self.subTest(key=key, value=value):
                data = copy.deepcopy(self.data)
                data["companies"][0]["scenario_sets"][0]["scenarios"][0][key] = value
                with self.assertRaises(MODULE.ValidationError):
                    MODULE.analyze(data)

    def test_duplicates_and_missing_central(self):
        variants = []
        duplicate_ids = copy.deepcopy(self.data)
        duplicate_ids["companies"][1]["id"] = duplicate_ids["companies"][0]["id"]
        variants.append(duplicate_ids)
        duplicate_scenarios = copy.deepcopy(self.data)
        duplicate_scenarios["companies"][0]["scenario_sets"][0]["scenarios"][1]["name"] = "bear"
        variants.append(duplicate_scenarios)
        missing_central = copy.deepcopy(self.data)
        missing_central["companies"][0]["scenario_sets"][0]["name"] = "other"
        variants.append(missing_central)
        duplicate_sets = copy.deepcopy(self.data)
        duplicate_sets["companies"][0]["scenario_sets"][1]["name"] = "central"
        variants.append(duplicate_sets)
        for data in variants:
            with self.assertRaises(MODULE.ValidationError):
                MODULE.analyze(data)

    def test_gates_do_not_round_and_evidence_is_not_verified(self):
        self.data["policy"]["min_success_probability"] = 0.80000000001
        result = MODULE.analyze(self.data)
        self.assertFalse(result["companies"][0]["eligible"])
        self.data["policy"]["min_success_probability"] = 0.6
        self.data["companies"][0]["evidence_eligible"] = False
        result = MODULE.analyze(self.data)
        self.assertIsNone(result["companies"][0]["rank"])
        self.assertTrue(any("attestation" in caveat for caveat in result["caveats"]))

    def test_cli_utf8_output_and_duplicate_key_rejection(self):
        directory = Path.cwd() / "work"
        directory.mkdir(exist_ok=True)
        unique_name = "scenario-test-" + uuid.uuid4().hex
        input_path = directory / (unique_name + "-input.json")
        output_path = directory / (unique_name + "-output.json")
        try:
            self.data["companies"][0]["name"] = "Fictional Caf\u00e9"
            input_path.write_text(json.dumps(self.data, ensure_ascii=False), encoding="utf-8")
            run = subprocess.run([sys.executable, str(SCRIPT), str(input_path), "--output", str(output_path)], capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(json.loads(output_path.read_text(encoding="utf-8"))["companies"][0]["name"], "Fictional Caf\u00e9")
            original_text = input_path.read_text(encoding="utf-8")
            run = subprocess.run([sys.executable, str(SCRIPT), str(input_path), "--output", str(input_path)], capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(run.returncode, 2)
            self.assertIn("must not overwrite input", run.stderr)
            self.assertEqual(input_path.read_text(encoding="utf-8"), original_text)
            input_path.write_text('{"schema_version":1,"schema_version":1}', encoding="utf-8")
            run = subprocess.run([sys.executable, str(SCRIPT), str(input_path)], capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(run.returncode, 2)
            self.assertIn("Duplicate JSON object key", run.stderr)
        finally:
            input_path.unlink(missing_ok=True)
            output_path.unlink(missing_ok=True)

    def test_source_snapshot_retained_and_input_not_mutated(self):
        original = copy.deepcopy(self.data)
        result = MODULE.analyze(self.data)
        self.assertEqual(self.data, original)
        self.assertEqual(result["companies"][0]["price"], original["companies"][0]["price"])
        for key, value in [("source_id", ""), ("as_of", "2026-02-30")]:
            data = copy.deepcopy(self.data)
            data["companies"][0]["price"][key] = value
            with self.assertRaises(MODULE.ValidationError):
                MODULE.analyze(data)

    def test_unknown_fields_rejected_at_each_level(self):
        for level in ("root", "policy", "company", "price", "set", "scenario"):
            data = copy.deepcopy(self.data)
            company = data["companies"][0]
            targets = {"root": data, "policy": data["policy"], "company": company,
                       "price": company["price"], "set": company["scenario_sets"][0],
                       "scenario": company["scenario_sets"][0]["scenarios"][0]}
            targets[level]["typo"] = 123
            with self.subTest(level=level), self.assertRaises(MODULE.ValidationError):
                MODULE.analyze(data)


if __name__ == "__main__":
    unittest.main()
