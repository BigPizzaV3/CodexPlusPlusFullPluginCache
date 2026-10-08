#!/usr/bin/env python3
"""Validate the complete V2 plugin package and preservation invariants."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "CONTENT_MANIFEST.json"
EXPECTED_MANUAL_SHA = "29ea3e38288ef618c5598d8958891c24947668a39f93d8852b6b528a8432bcc3"


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


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise ValueError("not a valid PNG header")
    return struct.unpack(">II", data[16:24])


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors = []
    manual = ROOT / "canonical" / data["source_document"]["bundled_filename"]
    if not is_file(manual) or sha256(manual) != EXPECTED_MANUAL_SHA:
        errors.append("canonical DOCX missing or hash mismatch")
    counts = {
        "modules": len(list((ROOT / "canonical" / "modules").glob("M*.md"))),
        "appendices": len(list((ROOT / "canonical" / "appendices").glob("Appendix-*.md"))),
        "master_labs": len(list((ROOT / "canonical" / "master-labs").glob("Master-Lab-*.md"))),
        "skills": len(list((ROOT / "skills").glob("*/SKILL.md"))),
        "sector_models": len(list((ROOT / "sector-models").glob("M*.model.json"))),
    }
    expected = {"modules": 106, "appendices": 13, "master_labs": 14, "skills": 28, "sector_models": 36}
    for key, value in expected.items():
        if counts[key] != value:
            errors.append(f"{key} count {counts[key]} != {value}")
    for path in (ROOT / "skills").glob("*/SKILL.md"):
        if not (path.parent / "agents" / "openai.yaml").is_file():
            errors.append(f"{path.parent.name}: agents/openai.yaml missing")
    for relative, digest in data.get("files", {}).items():
        path = ROOT / relative
        if not is_file(path):
            errors.append(f"missing manifested file: {relative}")
        elif sha256(path) != digest:
            errors.append(f"hash mismatch: {relative}")
    for relative in ["assets/composer-icon.png", "assets/logo.png"]:
        try:
            width, height = png_size(ROOT / relative)
            if width != height:
                errors.append(f"non-square marketplace asset: {relative} ({width}x{height})")
        except Exception as exc:
            errors.append(f"invalid marketplace asset {relative}: {exc}")
    plugin = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    if plugin.get("version") != "2.0.0" or plugin.get("name") != ROOT.name:
        errors.append("plugin identity/version mismatch")
    if "mcpServers" in plugin or (ROOT / ".mcp.json").exists():
        errors.append("unexpected MCP/server dependency")
    evals = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
    if evals.get("case_count", 0) < 100 or evals.get("case_count") != len(evals.get("cases", [])):
        errors.append("evaluation suite has fewer than 100 valid cases")
    baseline = data.get("baseline_preservation", {})
    if baseline.get("missing_files") or baseline.get("canonical_changes") or baseline.get("unexpected_changes"):
        errors.append("V1 baseline preservation report contains missing or unexpectedly changed files")
    result = {"ok": not errors, "errors": errors, "counts": counts,
              "evaluation_cases": evals.get("case_count"),
              "manual_sha256": sha256(manual) if is_file(manual) else None,
              "manifested_files": len(data.get("files", {}))}
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
