#!/usr/bin/env python3
"""Validate a research-state JSON file against required completion fields.

This is intentionally conservative. It checks presence/status, not the quality of evidence.
"""
from __future__ import annotations
import argparse, json, sys

REQUIRED = [
    "decision_question", "scope", "sources", "assumptions", "contrary_evidence",
    "risks", "scenarios", "valuation", "thesis_breaks", "completion_gates"
]

def validate(obj):
    errors = []
    for key in REQUIRED:
        if key not in obj:
            errors.append(f"missing required field: {key}")
    gates = obj.get("completion_gates", [])
    failed = [g for g in gates if isinstance(g, dict) and g.get("mandatory", True) and g.get("status") != "pass"]
    return errors, failed

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("path")
    ns = p.parse_args()
    obj = json.load(open(ns.path, encoding="utf-8"))
    errors, failed = validate(obj)
    print(json.dumps({"schema_errors": errors, "failed_mandatory_gates": failed, "complete": not errors and not failed}, indent=2))
    sys.exit(0 if not errors and not failed else 2)
