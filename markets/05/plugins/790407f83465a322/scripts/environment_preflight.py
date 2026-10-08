#!/usr/bin/env python3
"""Offline preflight for a discovered Power Apps Developer Environment."""
import argparse, json, re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Check Developer Environment discovery evidence")
    parser.add_argument("--environment-id", required=True)
    parser.add_argument("--display-name", required=True)
    parser.add_argument("--status", choices=("Ready", "Provisioning", "Blocked"), required=True)
    parser.add_argument("--dataverse-url", default="")
    parser.add_argument("--capacity-exceeded", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    issues = []
    if not re.fullmatch(r"[0-9a-fA-F-]{36}", args.environment_id):
        issues.append("Environment ID hat kein GUID-Format")
    if args.status != "Ready":
        issues.append(f"Umgebung ist noch nicht bereit: {args.status}")
    if args.capacity_exceeded:
        issues.append("Dataverse storage capacity exceeded")
    if args.dataverse_url and not re.fullmatch(r"https://[^/]+\.crm(?:\d+)?\.dynamics\.com/?", args.dataverse_url):
        issues.append("Dataverse URL hat kein erwartetes CRM-Format")
    result = {"environment": args.display_name, "environmentId": args.environment_id, "status": args.status, "dataverseUrl": args.dataverse_url or None, "readyForConnection": not issues and bool(args.dataverse_url), "issues": issues}
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("Developer Environment Preflight: " + ("PASS" if result["readyForConnection"] else "ACTION REQUIRED"))
        print(f"Environment: {args.display_name} ({args.environment_id})")
        notes = issues or ([] if args.dataverse_url else ["Dataverse URL fehlt noch; erst nach ihrer Ermittlung verbinden."])
        for issue in notes:
            print("- " + issue)
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
