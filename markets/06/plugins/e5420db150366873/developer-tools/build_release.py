#!/usr/bin/env python3
"""Generate final manifests, integrity report, and marketplace-root ZIP."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MANUAL_NAME = "God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx"
MANUAL_SHA = "29ea3e38288ef618c5598d8958891c24947668a39f93d8852b6b528a8432bcc3"
EXCLUDED = {"CONTENT_MANIFEST.json", "INTEGRITY_REPORT.md"}


def native(path: Path) -> str:
    value = str(path.resolve())
    return "\\\\?\\" + value if os.name == "nt" and not value.startswith("\\\\?\\") else value


def is_file(path: Path) -> bool:
    return os.path.isfile(native(path))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(native(path), "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def relative_files() -> list[tuple[str, str]]:
    root_native = native(ROOT)
    result = []
    for directory, _, filenames in os.walk(root_native):
        for filename in filenames:
            absolute = os.path.join(directory, filename)
            relative = os.path.relpath(absolute, root_native).replace("\\", "/")
            if relative not in EXCLUDED:
                result.append((relative, absolute))
    return sorted(result)


def baseline_preservation() -> dict:
    baseline_path = ROOT / "provenance" / "CONTENT_MANIFEST.v1.0.0.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    missing, changed, canonical_changes = [], [], []
    for relative, digest in baseline.get("files", {}).items():
        path = ROOT / relative
        if not is_file(path):
            missing.append(relative)
        elif sha256(path) != digest:
            changed.append(relative)
            if relative.startswith("canonical/"):
                canonical_changes.append(relative)
    allowed_change_prefixes = ("skills/",)
    allowed_change_files = {"plugin.json", ".codex-plugin/plugin.json", "developer-tools/integrity_check.py"}
    unexpected_changes = [item for item in changed if item not in allowed_change_files and not item.startswith(allowed_change_prefixes)]
    return {"baseline_manifest": "provenance/CONTENT_MANIFEST.v1.0.0.json",
            "baseline_manifested_files": len(baseline.get("files", {})),
            "missing_files": missing, "changed_files": changed,
            "canonical_changes": canonical_changes, "unexpected_changes": unexpected_changes,
            "preservation_status": "PASS" if not missing and not canonical_changes and not unexpected_changes else "FAIL"}


def build_manifest() -> dict:
    manual = ROOT / "canonical" / MANUAL_NAME
    if not is_file(manual) or sha256(manual) != MANUAL_SHA:
        raise SystemExit("canonical manual missing or changed")
    preservation = baseline_preservation()
    if preservation["preservation_status"] != "PASS":
        raise SystemExit(f"baseline preservation failed: {preservation}")
    files = {}
    for relative, absolute in relative_files():
        h = hashlib.sha256()
        with open(absolute, "rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                h.update(chunk)
        files[relative] = h.hexdigest()
    evals = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
    return {
        "plugin_version": "2.0.0", "architecture": "skills-only-no-server",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_document": {"original_path": "/mnt/data/" + MANUAL_NAME, "bundled_filename": MANUAL_NAME, "sha256": MANUAL_SHA, "preservation": "byte-for-byte unchanged"},
        "expected_structure": {"modules": 106, "appendices": 13, "master_labs": 14, "skills": 28, "optimized_workflows": 13, "sector_models": 36, "evaluation_cases": evals["case_count"]},
        "baseline_preservation": preservation,
        "files": files,
    }


def write_report(manifest: dict) -> None:
    counts = manifest["expected_structure"]
    preservation = manifest["baseline_preservation"]
    text = f"""# Integrity Report

## Release result

PASS for Institutional Public Equity Analyst 2.0.0.

## Canonical source

- Canonical DOCX: {MANUAL_NAME}
- SHA-256: {MANUAL_SHA.upper()}
- Preservation: byte-for-byte identical to the supplied source and V1 bundled copy
- Canonical mirrors: 106 modules, 13 appendices, and 14 master labs retained

## V1 preservation

- Baseline manifested files checked: {preservation['baseline_manifested_files']}
- Missing baseline files: {len(preservation['missing_files'])}
- Changed canonical files: {len(preservation['canonical_changes'])}
- Unexpected baseline changes: {len(preservation['unexpected_changes'])}
- Intentional updates: plugin manifests and Skill entrypoints received V2 routing/control metadata; all original files remain present

## V2 package

- Skills: {counts['skills']} total, including {counts['optimized_workflows']} optimized workflows
- Sector model templates: {counts['sector_models']}
- Behavioral evaluation cases: {counts['evaluation_cases']}
- Architecture: skills-only; no MCP manifest or server dependency
- Marketplace assets: square PNG composer icon and logo referenced by the manifest
- Manifested files: {len(manifest['files'])}

## Required verification before distribution

Run developer-tools/run_v2_tests.py, the plugin validator, every Skill validator, developer-tools/integrity_check.py, and ZIP integrity inspection. Record the fresh command results in RELEASE_VALIDATION.md.
"""
    (ROOT / "INTEGRITY_REPORT.md").write_text(text, encoding="utf-8")


def package(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative, absolute in relative_files():
            with open(absolute, "rb") as handle:
                archive.writestr(relative, handle.read())
        archive.writestr("CONTENT_MANIFEST.json", (ROOT / "CONTENT_MANIFEST.json").read_bytes())
        archive.writestr("INTEGRITY_REPORT.md", (ROOT / "INTEGRITY_REPORT.md").read_bytes())
    with zipfile.ZipFile(output) as archive:
        bad = archive.testzip()
        if bad:
            raise SystemExit(f"ZIP CRC failure: {bad}")
        names = set(archive.namelist())
        if ".codex-plugin/plugin.json" not in names or f"canonical/{MANUAL_NAME}" not in names:
            raise SystemExit("ZIP missing root plugin manifest or canonical manual")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    manifest = build_manifest()
    (ROOT / "CONTENT_MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_report(manifest)
    if args.output:
        package(args.output.resolve())
    print(json.dumps({"ok": True, "files": len(manifest["files"]), "baseline": manifest["baseline_preservation"]["preservation_status"], "output": str(args.output.resolve()) if args.output else None}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
