#!/usr/bin/env python3
"""Calculate declared planning readiness, not verified release readiness."""
import argparse
import json
from pathlib import Path
from blueprint_schema import load_blueprint


def truth(data, dotted):
    value = data
    for part in dotted.split("."):
        if not isinstance(value, dict):
            return False
        value = value.get(part)
    return bool(value)


def main():
    parser = argparse.ArgumentParser(description="Score a Dataverse app blueprint from 0 to 100")
    parser.add_argument("blueprint", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    try:
        data = load_blueprint(args.blueprint)
    except (OSError, ValueError) as exc:
        print(f"ERROR: Cannot read blueprint: {exc}")
        return 2

    pillars = {
        "Business value": (["business.outcome", "business.successMetrics", "business.baselines", "business.targets"], 15),
        "Data and security": (["dataModel.tables", "security.leastPrivilegeReviewed", "security.roleTaskMatrix", "security.fieldSecurityReviewed"], 20),
        "UX and accessibility": (["personas", "navigation", "forms", "views", "testing.keyboardTest", "testing.responsiveTest"], 20),
        "Performance": (["performance.expectedRecordVolume", "performance.formComponentBudget", "performance.representativeDataTest"], 15),
        "Change resilience": (["change.impactReviewed", "change.rollbackPlan"], 10),
        "ALM and evidence": (["alm.devUnmanaged", "alm.downstreamManaged", "alm.repositoryExport", "alm.version", "testing.roleSmokeTests"], 20),
    }
    detail, total, actions = [], 0, []
    for label, (checks, weight) in pillars.items():
        passed = sum(truth(data, check) for check in checks)
        points = round(weight * passed / len(checks))
        total += points
        missing = [check for check in checks if not truth(data, check)]
        detail.append({"pillar": label, "score": points, "maximum": weight, "missing": missing})
        actions.extend(f"{label}: {item} nachweisen" for item in missing)
    deprecated = data.get("modernization", {}).get("deprecatedComponents", [])
    if deprecated:
        total = max(0, total - min(10, len(deprecated) * 3))
        actions.append("Modernisierung: Deprecated Components ablösen oder Risikofreigabe dokumentieren")
    result = {"score": total, "releaseBand": "review-required" if total >= 75 else "blocked", "assessmentType": "declared-planning-readiness", "runtimeVerified": False, "pillars": detail, "actions": actions}
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"App Health Score: {total}/100 ({result['releaseBand']})")
        for item in detail:
            print(f"- {item['pillar']}: {item['score']}/{item['maximum']}")
        for action in actions:
            print("ACTION: " + action)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
