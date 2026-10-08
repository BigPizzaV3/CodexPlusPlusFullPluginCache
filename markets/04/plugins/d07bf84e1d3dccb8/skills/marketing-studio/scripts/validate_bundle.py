#!/usr/bin/env python3
"""Validate the bundled Marketing Studio repository snapshot."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = SKILL_ROOT / "references" / "catalog.json"
CODE_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
SEMVER_PATTERN = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$"
)
SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
)
REQUIRED_REFERENCES = {
    "references/catalog.md",
    "references/compatibility.md",
    "references/source-status.md",
    "references/ecommerce.md",
    "references/amazon.md",
    "references/tiktok-shop.md",
    "references/influencer.md",
    "references/shopee.md",
}
USER_PATH_MARKERS = (
    b"/" + b"Users" + b"/",
    b"/" + b"home" + b"/",
)


def load_catalog(path: Path = CATALOG_PATH) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError("catalog.json must contain an object")
    return payload


def resolve_reference(relative_path: str) -> Path:
    if not relative_path.startswith("references/"):
        raise ValueError(f"Reference must stay under references/: {relative_path}")
    candidate = (SKILL_ROOT / relative_path).resolve()
    references_root = (SKILL_ROOT / "references").resolve()
    if candidate == references_root or references_root not in candidate.parents:
        raise ValueError(f"Reference escapes the skill: {relative_path}")
    return candidate


def validate_catalog(payload: dict[str, Any]) -> int:
    if payload.get("schemaVersion") != 1:
        raise ValueError("catalog.json schemaVersion must be 1")
    snapshot = payload.get("snapshot")
    if not isinstance(snapshot, dict):
        raise ValueError("catalog.json snapshot must be an object")
    if snapshot.get("kind") != "repository-playbook-snapshot":
        raise ValueError("snapshot.kind must be repository-playbook-snapshot")
    if not SHA_PATTERN.fullmatch(str(snapshot.get("sourceRef", ""))):
        raise ValueError("snapshot.sourceRef must be a full Git commit")
    if snapshot.get("publicationVerified") is not False:
        raise ValueError("repository snapshot must not claim live publication")
    source_files = snapshot.get("sourceFiles")
    if not isinstance(source_files, list) or not source_files:
        raise ValueError("snapshot.sourceFiles must be a non-empty array")
    if any(
        not isinstance(path, str)
        or not path.startswith("backend/sql/")
        or ".." in Path(path).parts
        for path in source_files
    ):
        raise ValueError("snapshot.sourceFiles contains an unsafe source path")
    skills = payload.get("skills")
    if not isinstance(skills, list):
        raise ValueError("catalog.json skills must be an array")
    expected_count = snapshot.get("expectedCount")
    if expected_count != len(skills):
        raise ValueError(
            f"snapshot expectedCount={expected_count} but catalog has {len(skills)} entries"
        )
    codes: set[str] = set()
    for index, skill in enumerate(skills):
        if not isinstance(skill, dict):
            raise ValueError(f"skills[{index}] must be an object")
        code = str(skill.get("code", ""))
        if not CODE_PATTERN.fullmatch(code):
            raise ValueError(f"Invalid skill code: {code}")
        if code in codes:
            raise ValueError(f"Duplicate skill code: {code}")
        codes.add(code)
        if not str(skill.get("name", "")).strip():
            raise ValueError(f"Missing name for {code}")
        if not str(skill.get("platform", "")).strip():
            raise ValueError(f"Missing platform for {code}")
        if not str(skill.get("category", "")).strip():
            raise ValueError(f"Missing category for {code}")
        if not SEMVER_PATTERN.fullmatch(str(skill.get("version", ""))):
            raise ValueError(f"Invalid version for {code}")
        if not isinstance(skill.get("keywords"), list) or not skill["keywords"]:
            raise ValueError(f"Missing keywords for {code}")
        if not isinstance(skill.get("requires"), list):
            raise ValueError(f"requires must be an array for {code}")
        reference = str(skill.get("reference", ""))
        if not resolve_reference(reference).is_file():
            raise ValueError(f"Missing reference for {code}: {reference}")
    return len(skills)


def validate_files() -> None:
    skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    if "[TODO:" in skill_text:
        raise ValueError("SKILL.md contains an unresolved TODO")
    for reference in REQUIRED_REFERENCES:
        if not (SKILL_ROOT / reference).is_file():
            raise ValueError(f"Missing required reference: {reference}")
        if reference not in skill_text:
            raise ValueError(f"SKILL.md does not route to {reference}")
    for path in SKILL_ROOT.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Symlinks are not allowed: {path.relative_to(SKILL_ROOT)}")
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}:
            continue
        if not path.is_file():
            continue
        raw = path.read_bytes()
        if any(marker in raw for marker in USER_PATH_MARKERS):
            raise ValueError(f"User-specific path found in {path.relative_to(SKILL_ROOT)}")
        text = raw.decode("utf-8")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                raise ValueError(
                    f"Potential secret found in {path.relative_to(SKILL_ROOT)}"
                )


def validate() -> int:
    count = validate_catalog(load_catalog())
    validate_files()
    return count


def main() -> int:
    count = validate()
    print(f"Validated Marketing Studio bundle: {count} playbooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
