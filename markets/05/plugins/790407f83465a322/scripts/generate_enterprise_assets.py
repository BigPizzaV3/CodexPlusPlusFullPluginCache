#!/usr/bin/env python3
"""Generate reviewable enterprise delivery assets from a Dataverse app blueprint."""
import argparse
import json
from pathlib import Path
from blueprint_schema import load_blueprint
from execution_manifest import valid_solution


def write(path, text):
    path.write_text(text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Generate enterprise assets without credentials or tenant writes")
    parser.add_argument("blueprint", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    blueprint = load_blueprint(args.blueprint)
    solution = blueprint.get("solution", {}).get("uniqueName", "solution")
    if not valid_solution(solution):
        raise ValueError("Valid custom solution name required")
    personas = blueprint.get("personas", [])
    tables = blueprint.get("dataModel", {}).get("tables", [])
    args.output.mkdir(parents=True, exist_ok=False)

    template = Path(__file__).resolve().parents[1] / "assets/azure-pipelines.template.yml"
    write(args.output / "azure-pipelines.yml", template.read_text(encoding="utf-8").replace("__SOLUTION__", solution))
    tests = [f"- [ ] {p.get('role', p.get('name'))}: {task}" for p in personas for task in p.get("coreTasks", [])]
    write(args.output / "e2e-role-test-plan.md", "# E2E role test plan\n\n" + "\n".join(tests or ["- [ ] Define role tasks"]) + "\n\nRun on desktop, tablet, 200% zoom and keyboard-only navigation. Record run ID, role, result and evidence link.\n")
    catalog = {"solution": solution, "components": [{"table": t.get("logicalName"), "displayName": t.get("displayName"), "columns": [c.get("logicalName") for c in t.get("columns", [])]} for t in tables]}
    write(args.output / "component-catalog.json", json.dumps(catalog, ensure_ascii=False, indent=2) + "\n")
    write(args.output / "telemetry-contract.md", """# Telemetry contract

Capture app launch, navigation, save failure, integration failure, duration percentile and feature adoption. Store pseudonymous actor IDs only; never record field values, access tokens, prompts or sensitive data. Define retention, owner, alert thresholds and a data-subject deletion process before enabling collection.
""")
    write(args.output / "governance-portal-backlog.md", """# Governance portal backlog

- Change request: blueprint, impact score, target environments and approval.
- Evidence: validation, Solution Checker, accessibility, UAT and deployment run.
- Catalog: approved reusable tables, forms, views, role patterns and integration contracts.
- Operations: capacity, license, drift, adoption and failure alerts.
- Audit: immutable change ID, reviewer, decision, solution version and rollback reference.
""")
    write(args.output / "execution-runbook.md", f"""# Controlled execution runbook: {solution}

1. Confirm target URL, tenant, unmanaged Dev solution and approved blueprint hash.
2. Authenticate interactively or through an approved service connection; do not store credentials here.
3. Query current metadata and calculate a no-op-safe change plan.
4. Apply only confirmed additions/edits with supported Dataverse SDK, Web API or PAC operations.
5. Publish, export, unpack, compare against the blueprint and attach evidence.
6. Promote only managed packages after approval; keep prior package for rollback.
""")
    print(args.output)


if __name__ == "__main__":
    main()
