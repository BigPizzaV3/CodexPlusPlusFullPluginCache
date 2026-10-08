#!/usr/bin/env python3
"""Validate dependency-aware research state without third-party packages."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ALLOWED_MODULE = {"not_started", "in_progress", "blocked", "pass", "fail", "not_applicable"}
ALLOWED_GATE = {"open", "pass", "blocked", "fail"}


def validate(state: dict) -> dict:
    errors, warnings = [], []
    for key in ["company", "research_cutoff", "valuation_date", "workflow", "modules", "dependencies", "completion_status"]:
        if key not in state:
            errors.append(f"missing required field: {key}")
    modules = state.get("modules", {})
    for name, item in modules.items():
        if not isinstance(item, dict) or item.get("status") not in ALLOWED_MODULE:
            errors.append(f"module {name} has invalid status")
        if item.get("status") in {"blocked", "fail", "not_applicable"} and not item.get("reason"):
            errors.append(f"module {name} requires reason for status {item.get('status')}")
    gates = state.get("dependencies", [])
    known = set(modules) | {g.get("gate_id") for g in gates if isinstance(g, dict)}
    for gate in gates:
        if gate.get("status") not in ALLOWED_GATE:
            errors.append(f"gate {gate.get('gate_id')} has invalid status")
        missing = [dep for dep in gate.get("requires", []) if dep not in known]
        if missing:
            errors.append(f"gate {gate.get('gate_id')} has unknown dependencies: {missing}")
        if gate.get("status") == "pass":
            open_deps = [dep for dep in gate.get("requires", []) if dep in modules and modules[dep].get("status") not in {"pass", "not_applicable"}]
            if open_deps:
                errors.append(f"gate {gate.get('gate_id')} passed with open dependencies: {open_deps}")
        elif not gate.get("reason"):
            warnings.append(f"gate {gate.get('gate_id')} should explain non-pass status")
    open_items = [name for name, item in modules.items() if item.get("status") not in {"pass", "not_applicable"}]
    open_items += [g.get("gate_id") for g in gates if g.get("status") != "pass"]
    if state.get("completion_status") == "PASS" and open_items:
        errors.append("completion_status PASS conflicts with open modules or gates")
    return {"status": "PASS" if not errors and not open_items else "RESEARCH_INCOMPLETE",
            "errors": errors, "warnings": warnings, "open_items": open_items}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    state = json.loads(args.path.read_text(encoding="utf-8"))
    result = validate(state)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
