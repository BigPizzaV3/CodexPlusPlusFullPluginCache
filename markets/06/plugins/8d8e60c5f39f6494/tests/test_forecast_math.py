"""Invariant and failure-case tests for the bundled local calculator."""
import copy
from contextlib import contextmanager
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import shutil
import uuid
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "horizon-forecast" / "scripts" / "forecast_math.py"
spec = importlib.util.spec_from_file_location("forecast_math", SCRIPT)
fm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fm)


def candidate(name="A", value=3, confidence="medium"):
    return {"name": name, "confidence": confidence, "confidence_reason": "Synthetic evidence fixture",
            "growth": {k: value for k in fm.GROWTH},
            "overlooked": {k: value for k in fm.OVERLOOKED},
            "rationale": {k: "Synthetic fixture assumption, not real evidence" for k in [*fm.GROWTH, *fm.OVERLOOKED]}}


def score_input():
    return {"comparison_scope": "Synthetic global annual revenue in 2035", "candidates": [candidate()]}


def scenario_input():
    return {"market": "Fictional", "geography": "global", "metric": "annual producer revenue", "currency": "USD",
            "units": "billions", "price_basis": "constant 2025 USD", "baseline_source": "Synthetic fixture",
            "baseline_year": 2025, "horizon_year": 2035, "baseline_size": 100, "mode": "weighted",
            "partition_confirmed": True, "partition_definition": "Two exhaustive fictional states",
            "scenarios": [{"name": "down", "terminal_size": 50, "probability": .25, "assumptions": "Fixture down", "probability_basis": "Fixture"},
                          {"name": "up", "terminal_size": 250, "probability": .75, "assumptions": "Fixture up", "probability_basis": "Fixture"}]}


def calibration_input():
    return {"evaluation_date": "2026-09-15", "vintage_policy": "One synthetic snapshot per event, comparable lead time",
            "forecasts": [{"event_id": "A", "question": "Synthetic occurrence by deadline", "forecast_date": "2025-01-01",
                           "deadline": "2026-01-01", "resolution_rule": "Synthetic occurrence record", "probability": .8,
                           "outcome": 1, "resolved_on": "2026-01-02", "resolution_source": "Synthetic record", "baseline_probability": .5},
                          {"event_id": "B", "question": "Synthetic occurrence by deadline", "forecast_date": "2025-01-01",
                           "deadline": "2026-01-01", "resolution_rule": "Synthetic occurrence record", "probability": .4,
                           "outcome": 0, "resolved_on": "2026-01-02", "resolution_source": "Synthetic record", "baseline_probability": .5}]}


@contextmanager
def test_workspace():
    # Keep test writes in the caller's workspace, including in restricted desktops.
    parent = (Path.cwd() / "work" / "horizon-test-temp").resolve()
    parent.mkdir(parents=True, exist_ok=True)
    target = (parent / uuid.uuid4().hex).resolve()
    if not target.is_relative_to(parent) or target == parent:
        raise RuntimeError("Test scratch path escaped intended workspace")
    target.mkdir()
    try:
        yield str(target)
    finally:
        shutil.rmtree(target)


class ScoreTests(unittest.TestCase):
    def test_anchors(self):
        for val in (0, 3, 5):
            self.assertEqual(fm.rating({k: val for k in fm.GROWTH}, fm.GROWTH)["score"], val * 20)

    def test_missing_does_not_become_neutral(self):
        data = score_input()
        data["candidates"][0]["growth"]["scale"] = None
        row = fm.scores(data)["candidates"][0]
        self.assertIsNone(row["growth"]["score"])
        self.assertEqual(row["growth"]["bounds"], [45, 70])
        self.assertIsNone(row["rank"])

    def test_all_unknown(self):
        self.assertEqual(fm.rating(dict.fromkeys(fm.GROWTH), fm.GROWTH)["bounds"], [0, 100])

    def test_low_confidence_is_provisional(self):
        data = score_input()
        data["candidates"][0]["confidence"] = "low"
        self.assertIsNone(fm.scores(data)["candidates"][0]["rank"])

    def test_component_bounds_and_types(self):
        for val in (-1, 6, float("nan"), float("inf"), True, "3"):
            with self.subTest(value=val), self.assertRaises(ValueError):
                fm.rating({k: val for k in fm.GROWTH}, fm.GROWTH)

    def test_unknown_keys_fail(self):
        data = score_input()
        data["candidates"][0]["growth"]["fake"] = 4
        with self.assertRaises(ValueError): fm.scores(data)

    def test_invalid_weights_fail(self):
        data = score_input()
        data["growth_weights"] = {k: .1 for k in fm.GROWTH}
        with self.assertRaises(ValueError): fm.scores(data)

    def test_duplicate_candidates_fail(self):
        data = score_input()
        data["candidates"].append(candidate())
        with self.assertRaises(ValueError): fm.scores(data)

    def test_evidence_rationale_required(self):
        data = score_input()
        del data["candidates"][0]["rationale"]["demand"]
        with self.assertRaises(ValueError): fm.scores(data)

    def test_ties_are_not_alphabetical_winners(self):
        data = score_input()
        data["candidates"].append(candidate("B"))
        self.assertEqual([r["rank"] for r in fm.scores(data)["candidates"]], [1, 1])

    def test_weight_sensitivity_can_reverse_order(self):
        a, b = candidate("A"), candidate("B")
        a["growth"]["scale"] = 5
        a["growth"]["demand"] = 1
        b["growth"]["scale"] = 1
        b["growth"]["demand"] = 5
        rows = fm.scores({"comparison_scope": "fixture", "candidates": [a, b]})["candidates"]
        self.assertTrue(all(r["weight_sensitivity_rank_range"] == [1, 2] for r in rows))

    def test_overlooked_missing_does_not_hide_growth(self):
        data = score_input()
        data["candidates"][0]["overlooked"]["attention_gap"] = None
        row = fm.scores(data)["candidates"][0]
        self.assertEqual(row["rank"], 1)
        self.assertIsNone(row["overlooked"]["score"])


class ScenarioTests(unittest.TestCase):
    def test_expected_size_and_cagr_are_distinct(self):
        out = fm.scenarios(scenario_input())["expected"]
        self.assertEqual(out["terminal_size"], 200)
        self.assertEqual(out["added_annual_size"], 100)
        self.assertAlmostEqual(out["cagr_of_expected_terminal_size"], 2 ** .1 - 1)
        self.assertNotAlmostEqual(out["cagr_of_expected_terminal_size"], out["expected_cagr"])

    def test_probabilities_must_sum_to_one(self):
        data = scenario_input()
        data["scenarios"][0]["probability"] = .5
        with self.assertRaises(ValueError): fm.scenarios(data)

    def test_zero_baseline_has_no_cagr(self):
        data = scenario_input()
        data["baseline_size"] = 0
        out = fm.scenarios(data)
        self.assertIsNone(out["expected"]["expected_cagr"])
        self.assertIsNone(out["scenarios"][0]["cagr"])

    def test_missing_baseline_not_imputed(self):
        data = scenario_input()
        data["baseline_size"] = None
        with self.assertRaises(ValueError): fm.scenarios(data)

    def test_exploratory_has_no_expected_value(self):
        data = scenario_input()
        data["mode"] = "exploratory"
        for s in data["scenarios"]: s["probability"] = None
        self.assertIsNone(fm.scenarios(data)["expected"])

    def test_exploratory_rejects_implicit_weighting(self):
        data = scenario_input()
        data["mode"] = "exploratory"
        with self.assertRaises(ValueError): fm.scenarios(data)

    def test_negative_size_rejected(self):
        data = scenario_input()
        data["scenarios"][0]["terminal_size"] = -1
        with self.assertRaises(ValueError): fm.scenarios(data)

    def test_year_and_partition_requirements(self):
        for key, value in (("horizon_year", 2025), ("horizon_year", 2035.5), ("partition_confirmed", False)):
            data = scenario_input()
            data[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError): fm.scenarios(data)

    def test_zero_terminal_loss(self):
        self.assertEqual(fm.cagr(100, 0, 10), -1)


class CalibrationTests(unittest.TestCase):
    def test_brier_and_comparator(self):
        out = fm.calibrate(calibration_input())
        self.assertAlmostEqual(out["brier"], .1)
        self.assertAlmostEqual(out["comparator"]["skill_score"], .6)

    def test_missing_outcome_excluded(self):
        data = calibration_input()
        data["forecasts"][1]["outcome"] = None
        out = fm.calibrate(data)
        self.assertEqual(out["resolved_count"], 1)
        self.assertEqual(out["pending_count"], 1)
        self.assertAlmostEqual(out["brier"], .04)

    def test_duplicate_vintage_rejected(self):
        data = calibration_input()
        data["forecasts"].append(copy.deepcopy(data["forecasts"][0]))
        with self.assertRaises(ValueError): fm.calibrate(data)

    def test_future_resolution_rejected(self):
        data = calibration_input()
        data["forecasts"][0]["resolved_on"] = "2027-01-01"
        with self.assertRaises(ValueError): fm.calibrate(data)

    def test_forecast_at_deadline_rejected(self):
        data = calibration_input()
        data["forecasts"][0]["forecast_date"] = "2026-01-01"
        with self.assertRaises(ValueError): fm.calibrate(data)

    def test_comparator_uses_same_subset(self):
        data = calibration_input()
        del data["forecasts"][1]["baseline_probability"]
        out = fm.calibrate(data)["comparator"]
        self.assertEqual(out["n"], 1)
        self.assertAlmostEqual(out["model_brier_same_subset"], .04)

    def test_zero_baseline_loss_has_no_skill_ratio(self):
        data = calibration_input()
        for f in data["forecasts"]: f["baseline_probability"] = f["outcome"]
        self.assertIsNone(fm.calibrate(data)["comparator"]["skill_score"])

    def test_no_resolved_events(self):
        data = calibration_input()
        for f in data["forecasts"]: f["outcome"] = None
        self.assertIsNone(fm.calibrate(data)["brier"])

    def test_probability_one_in_final_bin(self):
        data = calibration_input()
        data["forecasts"][0]["probability"] = 1
        self.assertEqual(fm.calibrate(data)["reliability_bins"][-1]["n"], 1)


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)], capture_output=True, text=True)

    def test_output_created_and_not_overwritten(self):
        with test_workspace() as folder:
            input_path, output_path = Path(folder) / "in.json", Path(folder) / "out.json"
            input_path.write_text(json.dumps(scenario_input()), encoding="utf-8")
            first = self.run_cli("scenarios", input_path, "--output", output_path)
            self.assertEqual(first.returncode, 0, first.stderr)
            before = output_path.read_bytes()
            second = self.run_cli("scenarios", input_path, "--output", output_path)
            self.assertEqual(second.returncode, 2)
            self.assertEqual(before, output_path.read_bytes())

    def test_malformed_and_duplicate_json_rejected(self):
        with test_workspace() as folder:
            path = Path(folder) / "input.json"
            for content in ('{"a":1,"a":2}', '{"x":NaN}', '{broken'):
                path.write_text(content, encoding="utf-8")
                result = self.run_cli("scores", path)
                self.assertEqual(result.returncode, 2)

    def test_packaged_examples_run(self):
        for mode in ("scores", "scenarios", "calibrate"):
            result = self.run_cli(mode, ROOT / "examples" / f"{mode}-synthetic.json")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIsInstance(json.loads(result.stdout), dict)


if __name__ == "__main__":
    unittest.main()
