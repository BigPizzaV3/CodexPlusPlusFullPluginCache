from __future__ import annotations
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from research_audit import audit
from state_gate import validate


class StateTests(unittest.TestCase):
    def test_clean_state_passes(self):
        state = {"company": "Example", "research_cutoff": "2026-09-21", "valuation_date": "2026-09-21", "workflow": "test", "modules": {"scope": {"status": "pass"}}, "dependencies": [{"gate_id": "model", "requires": ["scope"], "status": "pass"}], "completion_status": "PASS"}
        self.assertEqual(validate(state)["status"], "PASS")

    def test_dependency_violation_fails(self):
        state = {"company": "Example", "research_cutoff": "2026-09-21", "valuation_date": "2026-09-21", "workflow": "test", "modules": {"scope": {"status": "blocked", "reason": "missing"}}, "dependencies": [{"gate_id": "model", "requires": ["scope"], "status": "pass"}], "completion_status": "PASS"}
        self.assertEqual(validate(state)["status"], "RESEARCH_INCOMPLETE")


class AuditTests(unittest.TestCase):
    def test_clean_bundle_passes(self):
        bundle = {"research_cutoff": "2026-09-21", "evidence": [{"evidence_id": "EVID-0001", "source_date": "2026-09-21", "freshness_category": "market_data"}], "claims": [{"claim_id": "C1", "classification": "reported_fact", "materiality": "high", "status": "verified"}], "edges": [{"from": "C1", "to": "EVID-0001", "relation": "supports"}], "definitions": [], "numeric_checks": [{"check_id": "N1", "pass": True}], "completion": {"workflow": "quarterly-update", "gates": [{"gate_id": "G1", "mandatory": True, "status": "pass"}]}}
        self.assertEqual(audit(bundle)["status"], "PASS")

    def test_unsupported_claim_fails(self):
        bundle = {"research_cutoff": "2026-09-21", "evidence": [], "claims": [{"claim_id": "C1", "classification": "reported_fact", "materiality": "critical", "status": "verified"}], "edges": [], "definitions": [], "numeric_checks": [], "completion": {"workflow": "quarterly-update", "gates": []}}
        self.assertEqual(audit(bundle)["status"], "RESEARCH_INCOMPLETE")

    def test_full_initiation_requires_appendix_m(self):
        bundle = {"research_cutoff": "2026-09-21", "evidence": [], "claims": [], "edges": [], "definitions": [], "numeric_checks": [], "completion": {"workflow": "full-company-initiation", "appendix_m_pass": False, "gates": []}}
        self.assertEqual(audit(bundle)["status"], "RESEARCH_INCOMPLETE")


if __name__ == "__main__":
    unittest.main()
