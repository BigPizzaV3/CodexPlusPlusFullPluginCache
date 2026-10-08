from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_artifacts_module():
    path = ROOT / "shared" / "artifacts.py"
    spec = importlib.util.spec_from_file_location("ib_artifacts", path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DashboardCitationReadinessPolicyTests(unittest.TestCase):
    def test_shared_dashboard_contract_helper_sets_readiness_policy(self) -> None:
        artifacts = load_artifacts_module()
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "contract.json"
            artifacts.write_dashboard_contract(
                path,
                "unit-test-skill",
                "Unit Test Report",
                "ExampleCo",
                "report_only",
                Path(tmpdir) / "report.html",
                report_body=[{"heading": "Summary", "body": "Draft body."}],
            )
            contract = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(contract["posture"], "draft")
        self.assertEqual(contract["citation_policy"], "block_for_senior")
        self.assertEqual(contract["metadata"]["readiness_posture"], "draft")
        self.assertEqual(contract["metadata"]["citation_policy"], "block_for_senior")


if __name__ == "__main__":
    unittest.main()
