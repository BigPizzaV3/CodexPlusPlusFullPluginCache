#!/usr/bin/env python3
"""Run citation, contradiction, freshness, definition, and completion audits."""
from __future__ import annotations
import argparse
import json
from datetime import date, datetime
from pathlib import Path

MATERIAL = {"high", "critical"}


def _parse_day(value: str) -> date:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).date()


def audit(bundle: dict) -> dict:
    failures, warnings, passes = [], [], []
    evidence = {item.get("evidence_id"): item for item in bundle.get("evidence", [])}
    claims = {item.get("claim_id"): item for item in bundle.get("claims", [])}
    edges = bundle.get("edges", [])
    support = {}
    contradiction = {}
    for edge in edges:
        if edge.get("relation") == "supports":
            support.setdefault(edge.get("from"), []).append(edge.get("to"))
        if edge.get("relation") == "contradicts":
            contradiction.setdefault(edge.get("to"), []).append(edge.get("from"))
    for claim_id, claim in claims.items():
        if claim.get("materiality") in MATERIAL:
            linked = [target for target in support.get(claim_id, []) if target in evidence]
            if claim.get("classification") in {"reported_fact", "management_claim", "external_estimate"} and not linked:
                failures.append({"audit": "citation", "claim_id": claim_id, "message": "material claim lacks direct evidence"})
            if claim.get("status") == "verified" and contradiction.get(claim_id):
                failures.append({"audit": "contradiction", "claim_id": claim_id, "message": "verified claim has unresolved contradiction edge"})
    passes.append(f"citation graph checked for {len(claims)} claims and {len(evidence)} evidence records")

    cutoff = bundle.get("research_cutoff")
    shelf = bundle.get("shelf_life_days", {"market_data": 1, "filing": 120, "guidance": 120, "capital_structure": 30, "management_role": 30, "industry": 365, "accounting_policy": 730})
    if cutoff:
        cutoff_day = _parse_day(cutoff)
        for evidence_id, item in evidence.items():
            category = item.get("freshness_category")
            if category in shelf and item.get("source_date"):
                age = (cutoff_day - _parse_day(item["source_date"])).days
                if age > shelf[category]:
                    failures.append({"audit": "freshness", "evidence_id": evidence_id, "message": f"stale by {age - shelf[category]} days"})

    definitions = bundle.get("definitions", [])
    seen = {}
    for item in definitions:
        key = (item.get("metric"), item.get("entity"), item.get("period"))
        value = (item.get("definition"), item.get("units"))
        if key in seen and seen[key] != value:
            failures.append({"audit": "definition", "key": key, "message": "conflicting definitions for same metric/entity/period"})
        seen[key] = value

    numeric_checks = bundle.get("numeric_checks", [])
    for check in numeric_checks:
        if not check.get("pass", False):
            failures.append({"audit": "numerical", "check_id": check.get("check_id"), "message": check.get("message", "numerical reconciliation failed")})

    completion = bundle.get("completion", {})
    for gate in completion.get("gates", []):
        if gate.get("mandatory", True) and gate.get("status") != "pass":
            failures.append({"audit": "completion", "gate_id": gate.get("gate_id"), "message": gate.get("reason", "mandatory gate not passed")})
    if completion.get("workflow") == "full-company-initiation" and not completion.get("appendix_m_pass", False):
        failures.append({"audit": "completion", "gate_id": "appendix_m", "message": "Appendix M not passed"})

    if not failures:
        passes.extend(["freshness audit passed", "definition audit passed", "numerical audit passed", "completion audit passed"])
    return {"status": "PASS" if not failures else "RESEARCH_INCOMPLETE", "passes": passes, "failures": failures, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    result = audit(json.loads(args.path.read_text(encoding="utf-8")))
    print(json.dumps(result, indent=2, default=str))
    return 0 if result["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
