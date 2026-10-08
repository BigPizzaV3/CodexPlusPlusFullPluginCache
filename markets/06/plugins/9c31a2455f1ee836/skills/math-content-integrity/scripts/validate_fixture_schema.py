#!/usr/bin/env python3
"""Lint fixture structure and required coverage; this is not a math renderer test."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


DEFAULT_FIXTURES = Path(__file__).with_name("math-contract-fixtures.json")
ALLOWED_TYPES = {"text", "currency", "math-inline", "math-block", "unresolved"}
ALLOWED_REGRESSION_KINDS = {"known-defect", "known-false-positive", "synthetic"}
REQUIRED_ISSUES = {
    "ambiguous-dollar",
    "unmatched-dollar",
    "bare-tex",
    "structured-block-omission",
    "malformed-latex",
    "generated-drift",
    "artifact-drift",
    "rendered-count-mismatch",
    "raw-browser-math-syntax",
}
REQUIRED_IDS = {
    "currency-basic",
    "inline-inequality",
    "numeric-math",
    "mixed-currency-math",
    "display-math",
    "currency-inside-explicit-math",
    "ambiguous-single-number",
    "unmatched-dollar",
    "bare-tex",
    "structured-block-omission",
    "malformed-latex",
    "generated-drift",
    "rendered-count-mismatch",
    "production-artifact-drift",
    "raw-browser-math-syntax",
}
REQUIRED_CASE_ISSUE = {
    "ambiguous-single-number": "ambiguous-dollar",
    "unmatched-dollar": "unmatched-dollar",
    "bare-tex": "bare-tex",
    "structured-block-omission": "structured-block-omission",
    "malformed-latex": "malformed-latex",
    "generated-drift": "generated-drift",
    "rendered-count-mismatch": "rendered-count-mismatch",
    "production-artifact-drift": "artifact-drift",
    "raw-browser-math-syntax": "raw-browser-math-syntax",
}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    fixtures = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_FIXTURES
    cases = json.loads(fixtures.read_text(encoding="utf-8"))
    if not isinstance(cases, list) or not cases:
        fail("fixture file must contain a non-empty array")

    seen: set[str] = set()
    seen_issues: set[str] = set()
    seen_regression_kinds: set[str] = set()
    pass_count = 0
    block_count = 0
    for case in cases:
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            fail("every fixture requires a non-empty id")
        if case_id in seen:
            fail(f"duplicate fixture id: {case_id}")
        seen.add(case_id)

        regression_kind = case.get("regressionKind")
        if regression_kind not in ALLOWED_REGRESSION_KINDS:
            fail(f"{case_id}: regressionKind must identify a known defect, known false positive, or synthetic case")
        seen_regression_kinds.add(regression_kind)
        source_reference = case.get("sourceReference")
        if not isinstance(source_reference, str) or not source_reference.strip():
            fail(f"{case_id}: sourceReference is required")

        evidence = case.get("sourceEvidence")
        if not isinstance(evidence, str) or not evidence.strip():
            fail(f"{case_id}: sourceEvidence is required")
        if not isinstance(case.get("input"), str) or not case["input"]:
            fail(f"{case_id}: input is required")

        outcome = case.get("expected")
        if outcome not in {"valid", "invalid"}:
            fail(f"{case_id}: expected must be valid or invalid")
        issues = case.get("issues")
        if not isinstance(issues, list):
            fail(f"{case_id}: issues must be an array")
        for issue in issues:
            issue_type = issue.get("type")
            reason = issue.get("reason")
            if not isinstance(issue_type, str) or not issue_type:
                fail(f"{case_id}: issue type is required")
            if not isinstance(reason, str) or not reason:
                fail(f"{case_id}: issue reason is required")
            seen_issues.add(issue_type)
        if outcome == "valid" and issues:
            fail(f"{case_id}: valid fixture must not declare issues")
        if outcome == "invalid" and not issues:
            fail(f"{case_id}: invalid fixture must declare an issue")
        issue_types = {issue["type"] for issue in issues}
        required_issue = REQUIRED_CASE_ISSUE.get(case_id)
        if required_issue and required_issue not in issue_types:
            fail(f"{case_id}: required issue type is {required_issue}")

        segments = case.get("segments")
        if not isinstance(segments, list) or not segments:
            fail(f"{case_id}: segments must be a non-empty array")
        unresolved = 0
        for segment in segments:
            segment_type = segment.get("type")
            if segment_type not in ALLOWED_TYPES:
                fail(f"{case_id}: unsupported segment type {segment_type!r}")
            if segment_type in {"text", "currency", "unresolved"}:
                value = segment.get("value")
                if not isinstance(value, str) or not value:
                    fail(f"{case_id}: {segment_type} requires a non-empty value")
            else:
                latex = segment.get("latex")
                if not isinstance(latex, str) or not latex:
                    fail(f"{case_id}: {segment_type} requires non-empty latex")
                if latex.startswith("$") or latex.endswith("$"):
                    fail(f"{case_id}: typed math must not retain dollar delimiters")
            if segment_type == "currency" and not segment["value"].startswith("$"):
                fail(f"{case_id}: currency must preserve its visible dollar sign")
            if segment_type == "unresolved":
                unresolved += 1
                reason = segment.get("reason")
                if not isinstance(reason, str) or not reason:
                    fail(f"{case_id}: unresolved segment requires a reason")
        if outcome == "valid" and unresolved:
            fail(f"{case_id}: valid fixture contains unresolved content")
        if issue_types.intersection({"ambiguous-dollar", "unmatched-dollar", "bare-tex"}) and not unresolved:
            fail(f"{case_id}: ambiguity and bare-TeX fixtures require an unresolved segment")

        if any(issue["type"] == "structured-block-omission" for issue in issues):
            count_keys = {"sourceBlockCount", "generatedBlockCount", "renderedBlockCount"}
            if not count_keys.issubset(case):
                fail(f"{case_id}: structured block counts are required")
            if not all(isinstance(case[key], int) and case[key] >= 0 for key in count_keys):
                fail(f"{case_id}: structured block counts must be non-negative integers")
            if case["sourceBlockCount"] == case["renderedBlockCount"]:
                fail(f"{case_id}: structured-block fixture has no rendered mismatch")

        if any(issue["type"] == "generated-drift" for issue in issues):
            source_hash = case.get("sourceProjectionHash")
            generated_hash = case.get("generatedProjectionHash")
            if not all(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) for value in (source_hash, generated_hash)):
                fail(f"{case_id}: two SHA-256 projection hashes are required")
            if source_hash == generated_hash:
                fail(f"{case_id}: generated-drift fixture has identical hashes")

        if any(issue["type"] == "artifact-drift" for issue in issues):
            source_hash = case.get("sourceProjectionHash")
            artifact_hash = case.get("artifactProjectionHash")
            if not all(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) for value in (source_hash, artifact_hash)):
                fail(f"{case_id}: source and artifact SHA-256 projection hashes are required")
            if source_hash == artifact_hash:
                fail(f"{case_id}: artifact-drift fixture has identical hashes")

        if any(issue["type"] in {"rendered-count-mismatch", "raw-browser-math-syntax"} for issue in issues):
            expected_count = case.get("expectedMathExpressionCount")
            rendered_count = case.get("renderedKatexRootCount")
            if not all(isinstance(value, int) and value >= 0 for value in (expected_count, rendered_count)):
                fail(f"{case_id}: non-negative expected and rendered counts are required")
            if expected_count == rendered_count:
                fail(f"{case_id}: rendered-count fixture has no mismatch")

        pass_count += int(outcome == "valid")
        block_count += int(outcome == "invalid")

    missing_ids = REQUIRED_IDS - seen
    if missing_ids:
        fail(f"missing required fixtures: {', '.join(sorted(missing_ids))}")
    missing_issues = REQUIRED_ISSUES - seen_issues
    if missing_issues:
        fail(f"missing required issue coverage: {', '.join(sorted(missing_issues))}")
    missing_regression_kinds = {"known-defect", "known-false-positive"} - seen_regression_kinds
    if missing_regression_kinds:
        fail(f"missing required regression coverage: {', '.join(sorted(missing_regression_kinds))}")
    print(f"PASS: fixture schema covers {len(cases)} cases ({pass_count} valid, {block_count} invalid)")


if __name__ == "__main__":
    main()
