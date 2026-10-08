#!/usr/bin/env python3
"""Offline quality gates for a Dataverse model-driven app blueprint."""
import argparse
import json
from pathlib import Path
from blueprint_schema import validate_blueprint


def present(data, path):
    value = data
    for key in path.split("."):
        if not isinstance(value, dict) or not value.get(key):
            return False
        value = value[key]
    return True


def main():
    parser = argparse.ArgumentParser(description="Validate a Dataverse app blueprint")
    parser.add_argument("blueprint", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    try:
        data = json.loads(args.blueprint.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: Cannot read blueprint: {exc}")
        return 2

    errors, warnings = validate_blueprint(data), []
    if errors:
        print(json.dumps({"valid": False, "errors": errors, "warnings": []}, indent=2))
        return 1
    required = {
        "G0 Scope": ["appName", "business.outcome", "business.successMetrics", "personas"],
        "G1 Data": ["solution.uniqueName", "solution.publisherPrefix", "dataModel.tables"],
        "G2 Security": ["security.leastPrivilegeReviewed", "security.roleTaskMatrix"],
        "G3 UX": ["navigation", "forms", "views"],
        "G5 Performance": ["performance.expectedRecordVolume", "performance.representativeDataTest"],
        "G6 Change": ["change.impactReviewed", "change.rollbackPlan"],
        "G7 ALM": ["alm.devUnmanaged", "alm.downstreamManaged", "alm.repositoryExport", "alm.version"],
    }
    for gate, paths in required.items():
        missing = [path for path in paths if not present(data, path)]
        if missing:
            errors.append(f"{gate}: fehlend/leer: {', '.join(missing)}")

    if not present(data, "testing.keyboardTest") or not present(data, "testing.responsiveTest"):
        errors.append("G4 Accessibility: keyboardTest und responsiveTest mÃ¼ssen geplant sein")
    if data.get("customPages") and not present(data, "testing.accessibilityPlan"):
        errors.append("G4 Accessibility: Custom Pages benÃ¶tigen testing.accessibilityPlan")
    for form in data.get("forms", []):
        fields = form.get("primaryTaskFields", [])
        if len(fields) > 12:
            warnings.append(f"Form '{form.get('name', '?')}' enthÃ¤lt {len(fields)} Felder auf dem ersten Tab; Aufgabenfokus prÃ¼fen")
    for view in data.get("views", []):
        columns = view.get("columns", [])
        if len(columns) > 10:
            warnings.append(f"View '{view.get('name', '?')}' enthÃ¤lt {len(columns)} Spalten; Scanbarkeit prÃ¼fen")
    for table in data.get("dataModel", {}).get("tables", []):
        name = table.get("logicalName", "")
        if name.startswith("new_"):
            warnings.append(f"Tabelle '{name}' nutzt das generische PrÃ¤fix 'new_'; bestÃ¤tigten Publisher-PrÃ¤fix verwenden")

    result = {"valid": not errors, "errors": errors, "warnings": warnings}
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("Blueprint Quality Gates: " + ("PASS" if result["valid"] else "FAIL"))
        for message in errors:
            print("ERROR: " + message)
        for message in warnings:
            print("WARNING: " + message)
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
