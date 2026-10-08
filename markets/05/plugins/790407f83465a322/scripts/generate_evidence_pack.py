#!/usr/bin/env python3
"""Create a human-reviewable accessibility and release evidence pack."""
import argparse
import json
from pathlib import Path


def mark(value):
    return "Nachweis geplant" if value else "FEHLT"


def main():
    parser = argparse.ArgumentParser(description="Generate a Dataverse app evidence pack")
    parser.add_argument("blueprint", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        data = json.loads(args.blueprint.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: Cannot read blueprint: {exc}")
        return 2
    test = data.get("testing", {})
    lines = [
        f"# Evidence Pack: {data.get('appName', 'Unbenannte App')}", "",
        "## Kontext", f"- Solution: {data.get('solution', {}).get('uniqueName', 'FEHLT')}",
        f"- UAT Owner: {test.get('uatOwner', 'FEHLT')}", "",
        "## Accessibility & Responsive", f"- Tastaturfluss: {mark(test.get('keyboardTest'))}",
        f"- Responsive/Zoom: {mark(test.get('responsiveTest'))}",
        f"- Accessibility-Plan: {test.get('accessibilityPlan', 'FEHLT')}", "",
        "## Rollen & Release", f"- Rollen-Smoke-Tests: {mark(test.get('roleSmokeTests'))}",
        f"- Least Privilege geprüft: {mark(data.get('security', {}).get('leastPrivilegeReviewed'))}",
        f"- Rollback: {data.get('change', {}).get('rollbackPlan', 'FEHLT')}",
        f"- Repository-Export: {mark(data.get('alm', {}).get('repositoryExport'))}", "",
        "## Sign-off", "- [ ] Fachliche UAT durchgeführt", "- [ ] Accessibility-Test durchgeführt", "- [ ] Security-/Rollen-Test durchgeführt", "- [ ] Validate/Publish erfolgreich", "- [ ] Rollback-Schritt verifiziert", "",
        "Hinweis: Dieses Dokument ist ein Prüfprotokoll. Häkchen dürfen erst nach tatsächlich ausgeführten Tests gesetzt werden.",
    ]
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Evidence pack written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
