#!/usr/bin/env python3
"""Summarize user-facing and operational impact between two app blueprints."""
import argparse
import json
from pathlib import Path


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def names(items, key):
    return {item.get(key, "") for item in items if isinstance(item, dict) and item.get(key)}


def diff(label, before, after, key, impacts):
    removed, added = names(before, key) - names(after, key), names(after, key) - names(before, key)
    for value in sorted(added):
        impacts.append(("MEDIUM", f"{label} hinzugefügt: {value}"))
    for value in sorted(removed):
        impacts.append(("HIGH", f"{label} entfernt: {value} — Abhängigkeiten und Rollback prüfen"))


def main():
    parser = argparse.ArgumentParser(description="Compare two Dataverse app blueprints")
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    args = parser.parse_args()
    try:
        before, after = load(args.before), load(args.after)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: Cannot read blueprint: {exc}")
        return 2
    impacts = []
    diff("Persona", before.get("personas", []), after.get("personas", []), "name", impacts)
    diff("Tabelle", before.get("dataModel", {}).get("tables", []), after.get("dataModel", {}).get("tables", []), "logicalName", impacts)
    diff("Formular", before.get("forms", []), after.get("forms", []), "name", impacts)
    diff("Ansicht", before.get("views", []), after.get("views", []), "name", impacts)
    old_groups = names(before.get("navigation", []), "group")
    new_groups = names(after.get("navigation", []), "group")
    for group in sorted(old_groups - new_groups):
        impacts.append(("HIGH", f"Navigationsgruppe entfernt: {group} — Nutzerkommunikation und Alternativpfad erforderlich"))
    if before.get("security") != after.get("security"):
        impacts.append(("HIGH", "Security-Konzept geändert — Rollen- und Zugriffstests erforderlich"))
    if before.get("solution", {}).get("uniqueName") != after.get("solution", {}).get("uniqueName"):
        impacts.append(("HIGH", "Solution geändert — Ziel, Abhängigkeiten und Deployment-Route bestätigen"))
    print("Change Impact Report")
    if not impacts:
        print("- Keine strukturellen Änderungen im Blueprint erkannt; Detailänderungen trotzdem testen.")
    for severity, text in impacts:
        print(f"- [{severity}] {text}")
    print("- [REQUIRED] Vor Publikation Validate/Publish, Rollentests und den dokumentierten Rollback ausführen.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
