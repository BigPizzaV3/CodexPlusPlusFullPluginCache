#!/usr/bin/env python3
"""Validate deterministic fields in a Skills-only submission pack JSON."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any


PACKAGE_NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)


def normalized_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    return " ".join(value.split()).casefold()


def one_line(value: str) -> bool:
    return "\n" not in value and "\r" not in value


def require_string(data: dict[str, Any], key: str, issues: list[str]) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        issues.append(f"{key}: required non-empty string")
        return ""
    return value


def validate_case(case: Any, label: str, negative: bool, issues: list[str]) -> None:
    if not isinstance(case, dict):
        issues.append(f"{label}: must be an object")
        return
    required = [
        "prompt",
        "fixture",
        "expected_activation",
        "expected_behavior",
        "expected_result_shape",
        "actual_result_summary",
        "evidence_ref",
    ]
    if negative:
        required.append("reason")
    for key in required:
        value = case.get(key)
        if not isinstance(value, str) or not value.strip():
            issues.append(f"{label}.{key}: required non-empty string")
    if case.get("expected_activation") not in {"YES", "NO"}:
        issues.append(f"{label}.expected_activation: must be YES or NO")


def validate(data: dict[str, Any]) -> list[str]:
    issues: list[str] = []

    if data.get("pack_status") != "DRAFT_COMPLETE_FROM_SUPPLIED_EVIDENCE":
        issues.append("pack_status: complete validation requires DRAFT_COMPLETE_FROM_SUPPLIED_EVIDENCE")

    if data.get("artifact_use") not in {"SUBMISSION_DRAFT", "TEST_ONLY_NOT_FOR_SUBMISSION"}:
        issues.append("artifact_use: must be SUBMISSION_DRAFT or TEST_ONLY_NOT_FOR_SUBMISSION")

    if data.get("submission_type") != "skills-only":
        issues.append("submission_type: must be 'skills-only'")

    require_string(data, "package_digest", issues)
    require_string(data, "rule_snapshot", issues)

    package_name = require_string(data, "package_name", issues)
    if package_name and (len(package_name) > 64 or not PACKAGE_NAME_RE.fullmatch(package_name)):
        issues.append("package_name: max 64; ASCII letters, digits, '_' or '-'; start alphanumeric")

    skill_name = require_string(data, "skill_name", issues)
    if skill_name and (len(skill_name) > 64 or not PACKAGE_NAME_RE.fullmatch(skill_name)):
        issues.append("skill_name: max 64; ASCII letters, digits, '_' or '-'; start alphanumeric")
    if package_name and skill_name and len(f"{package_name}:{skill_name}") > 64:
        issues.append("combined_identity: package_name:skill_name must be at most 64 characters")

    version = require_string(data, "version", issues)
    if version and (len(version) > 64 or not SEMVER_RE.fullmatch(version)):
        issues.append("version: must be semantic version and at most 64 characters")

    scalar_rules = {
        "display_name": (30, True),
        "short_description": (30, True),
        "long_description": (4000, False),
        "skill_description": (1024, False),
        "developer_name": (80, True),
        "category": (120, True),
        "release_notes": (4000, False),
        "independent_verdict": (64, True),
    }
    for key, (limit, must_be_one_line) in scalar_rules.items():
        value = require_string(data, key, issues)
        if value and len(value) > limit:
            issues.append(f"{key}: exceeds {limit} characters")
        if value and must_be_one_line and not one_line(value):
            issues.append(f"{key}: must be one line")

    capabilities = data.get("capabilities")
    if not isinstance(capabilities, list) or not capabilities:
        issues.append("capabilities: require 1 to 20 entries")
    elif len(capabilities) > 20:
        issues.append("capabilities: at most 20 entries")
    else:
        for index, value in enumerate(capabilities, 1):
            if not isinstance(value, str) or not value.strip():
                issues.append(f"capabilities[{index}]: required non-empty string")
            elif len(value) > 120 or not one_line(value):
                issues.append(f"capabilities[{index}]: one line and at most 120 characters")

    prompts = data.get("starter_prompts")
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3:
        issues.append("starter_prompts: require 1 to 3 entries")
    else:
        seen: set[str] = set()
        for index, value in enumerate(prompts, 1):
            if not isinstance(value, str) or not value.strip():
                issues.append(f"starter_prompts[{index}]: required non-empty string")
                continue
            if len(value) > 128 or not one_line(value):
                issues.append(f"starter_prompts[{index}]: one line and at most 128 characters")
            if "@" in value:
                issues.append(f"starter_prompts[{index}]: must not contain an @mention")
            normalized = normalized_text(value)
            if normalized in seen:
                issues.append(f"starter_prompts[{index}]: duplicate after normalization")
            seen.add(normalized)

    positive = data.get("positive_cases")
    if not isinstance(positive, list) or len(positive) != 5:
        issues.append("positive_cases: require exactly 5 executed cases")
    else:
        for index, case in enumerate(positive, 1):
            validate_case(case, f"positive_cases[{index}]", False, issues)

    negative = data.get("negative_cases")
    if not isinstance(negative, list) or len(negative) != 3:
        issues.append("negative_cases: require exactly 3 executed cases")
    else:
        for index, case in enumerate(negative, 1):
            validate_case(case, f"negative_cases[{index}]", True, issues)

    return issues


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_submission_pack.py submission-pack.json", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "issues": [str(exc)]}, ensure_ascii=False, indent=2))
        return 1
    if not isinstance(data, dict):
        issues = ["root: must be a JSON object"]
    else:
        issues = validate(data)
    status = "PASS" if not issues else "FAIL"
    print(json.dumps({"status": status, "issues": issues}, ensure_ascii=False, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
