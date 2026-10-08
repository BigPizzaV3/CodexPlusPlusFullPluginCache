#!/usr/bin/env python3
"""Generate a concise, reviewable UAT, security, ALM and test-data delivery pack from a blueprint."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Generate a Dataverse app delivery pack")
    parser.add_argument("blueprint", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.blueprint.read_text(encoding="utf-8"))
    lines = [f"# Delivery pack – {data.get('appName', 'Dataverse app')}", "", "## Roles and core tasks", ""]
    for persona in data.get("personas", []):
        lines.append(f"- **{persona.get('role', persona.get('name'))}**: " + ", ".join(persona.get("coreTasks", [])))
    lines += ["", "## UAT smoke tests", ""]
    for persona in data.get("personas", []):
        for task in persona.get("coreTasks", []):
            lines.append(f"- [ ] {persona.get('name')}: {task}")
    lines += ["", "## Release checklist", "", "- [ ] Environment and solution confirmed", "- [ ] Blueprint validation passed", "- [ ] Solution-vs-blueprint validation passed", "- [ ] Forms, views, keyboard flow and responsive layout tested", "- [ ] Unmanaged export committed; managed deployment package prepared", "", "## Test-data policy", ""]
    test_data = data.get("testData", {})
    lines.append(f"- Demo records: {test_data.get('records', 0)}. Cleanup: {test_data.get('cleanupMode', 'not specified')}. Never delete data without fresh explicit confirmation.")
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
