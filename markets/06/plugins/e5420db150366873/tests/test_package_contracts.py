from __future__ import annotations
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackageContractTests(unittest.TestCase):
    def test_manual_hash_declared(self):
        manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], "2.0.0")

    def test_100_plus_eval_cases(self):
        data = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(data["case_count"], 100)
        self.assertEqual(data["case_count"], len(data["cases"]))
        ids = [case["id"] for case in data["cases"]]
        self.assertEqual(len(ids), len(set(ids)))
        for case in data["cases"]:
            self.assertTrue(case["prompt"])
            self.assertTrue(case["expected"]["must"])
            self.assertTrue(case["expected"]["must_not"])

    def test_36_sector_models(self):
        models = list((ROOT / "sector-models").glob("M*.model.json"))
        self.assertEqual(len(models), 36)
        for path in models:
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertTrue(data["required_kpis"])
            self.assertGreaterEqual(len(data["preferred_valuation_methods"]), 3)
            self.assertTrue(data["stress_variables"])

    def test_optimized_workflows(self):
        required = {"full-company-initiation", "quarterly-update", "earnings-preview", "earnings-postmortem", "ten-k-deep-read", "forensic-screen", "management-review", "industry-map", "peer-comparison", "reverse-dcf", "risk-stress-test", "thesis-red-team", "short-thesis-red-team"}
        present = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
        self.assertTrue(required <= present)

    def test_skills_have_frontmatter(self):
        for path in (ROOT / "skills").glob("*/SKILL.md"):
            text = path.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), path)
            self.assertRegex(text, r"(?m)^name: [a-z0-9-]+$")
            self.assertRegex(text, r"(?m)^description: .+$")

    def test_no_server_dependency(self):
        self.assertFalse((ROOT / ".mcp.json").exists())
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertNotIn("mcpServers", manifest)


if __name__ == "__main__":
    unittest.main()
