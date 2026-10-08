#!/usr/bin/env python3
"""Generate a portable, evidence-first change capsule from blueprint and manifest."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Create a reviewable Dataverse change capsule")
    parser.add_argument("blueprint", type=Path)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    blueprint = json.loads(args.blueprint.read_text(encoding="utf-8"))
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    args.output.mkdir(parents=True, exist_ok=True)
    capsule = {"changeId": manifest.get("changeId"), "solution": manifest.get("solutionUniqueName"), "targetUrl": manifest.get("targetUrl"), "approvedBy": manifest.get("approvedBy"), "blueprintHash": hashlib.sha256(args.blueprint.read_bytes()).hexdigest(), "manifestHash": hashlib.sha256(args.manifest.read_bytes()).hexdigest(), "app": blueprint.get("appName"), "operations": manifest.get("operations", []), "gates": ["preflight", "manifest", "export/unpack", "blueprint comparison", "role test", "approval"]}
    (args.output / "change-capsule.json").write_text(json.dumps(capsule, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.output / "CHANGE-RECORD.md").write_text(f"# Change {capsule['changeId']}\n\n- Solution: `{capsule['solution']}`\n- App: {capsule['app']}\n- Approved by: {capsule['approvedBy']}\n- Blueprint hash: `{capsule['blueprintHash']}`\n- Manifest hash: `{capsule['manifestHash']}`\n\n## Required gates\n" + "\n".join(f"- [ ] {gate}" for gate in capsule["gates"]) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
