#!/usr/bin/env python3
"""Check review authority and bindings; this does not authenticate a tool response."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


HASH = re.compile(r"[0-9a-f]{64}")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_review(result: object, *, project_id: str | None = None,
                    run_id: str | None = None, revision: int | None = None,
                    input_hash: str | None = None, asset_hashes: dict[str, str] | None = None,
                    require_paid: bool = False, require_paid_pass: bool = False) -> str:
    require(isinstance(result, dict), "review must be the exact response object")
    authority = result.get("reviewAuthority")
    if authority == "deterministic_basic":
        require(not require_paid and not require_paid_pass, "basic checks cannot supply a paid review or PASS")
        require(result.get("serverAiUsed") is False, "basic checks cannot claim server AI")
        require("paidReviewReceipt" in result and result["paidReviewReceipt"] is None,
                "basic checks must have a null paidReviewReceipt")
        require(result.get("status") in {"guidance", "consistent", "changes_requested"},
                "basic status cannot claim creative PASS")
        require(result.get("judgment") in {"lp_route_consistency", "video_expression", "video_fit"},
                "unknown basic judgment")
        require(not any(key in result for key in ("receiptHash", "reviewId", "projectId")),
                "basic response cannot carry a paid receipt or project")
        return authority
    require(authority == "paid_server", "missing server review authority")
    for field in ("reviewId", "runId", "projectId", "policyVersion", "model", "summary"):
        require(isinstance(result.get(field), str) and bool(result[field].strip()), f"missing paid {field}")
    for field in ("inputHash", "receiptHash"):
        require(isinstance(result.get(field), str) and HASH.fullmatch(result[field]) is not None,
                f"invalid paid {field}")
    require(type(result.get("revision")) is int and result["revision"] >= 0, "invalid paid revision")
    require(isinstance(result.get("assetHashes"), dict)
            and all(isinstance(key, str) and key and isinstance(value, str) and HASH.fullmatch(value)
                    for key, value in result["assetHashes"].items()),
            "invalid asset hashes")
    require(result.get("scope") in {"text", "image", "sampled_video"}, "invalid review scope")
    require(result.get("status") in {"passed", "changes_requested", "needs_review"}, "unfinished review")
    human_review = result.get("requiresHumanReview")
    require(isinstance(human_review, list) and bool(human_review)
            and all(item in {"final_approval", "continuous_motion", "audio_content", "final_viewing_and_approval"}
                    for item in human_review), "human-review requirement missing")
    require(isinstance(result.get("findings"), list), "review findings missing")
    for finding in result["findings"]:
        require(isinstance(finding, dict) and finding.get("severity") in {"blocking", "improvement", "unverified"},
                "invalid finding")
        require(all(isinstance(finding.get(field), str) and finding[field].strip()
                    for field in ("location", "reason", "instruction")), "incomplete finding")
    if project_id is not None:
        require(result["projectId"] == project_id, "review project mismatch")
    if run_id is not None:
        require(result["runId"] == run_id, "review run mismatch")
    if revision is not None:
        require(result["revision"] == revision, "stale review revision")
    if input_hash is not None:
        require(result["inputHash"] == input_hash, "review input mismatch")
    if asset_hashes is not None:
        require(result["assetHashes"] == asset_hashes, "review assets mismatch")
    if result["scope"] == "sampled_video":
        require(set(human_review) >= {"continuous_motion", "audio_content", "final_viewing_and_approval"}
                and result["status"] != "passed",
                "sampled video cannot certify full-video PASS")
    if result["status"] == "passed":
        require(human_review == ["final_approval"], "unverified media cannot PASS")
        require(not any(item["severity"] in {"blocking", "unverified"} for item in result["findings"]),
                "blocking or unverified findings cannot PASS")
    if require_paid_pass:
        require(result["status"] == "passed", "paid result is not passed")
    return authority


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("result", type=Path)
    parser.add_argument("--project-id")
    parser.add_argument("--run-id")
    parser.add_argument("--revision", type=int)
    parser.add_argument("--input-hash")
    parser.add_argument("--asset-hashes-file", type=Path)
    parser.add_argument("--require-paid", action="store_true")
    parser.add_argument("--require-paid-pass", action="store_true")
    args = parser.parse_args()
    try:
        if args.require_paid or args.require_paid_pass:
            require(args.project_id is not None and args.run_id is not None and args.revision is not None,
                    "paid validation requires expected project, run and revision")
            require(args.input_hash is not None and args.asset_hashes_file is not None,
                    "paid validation requires expected input hash and asset hashes")
        asset_hashes = json.loads(args.asset_hashes_file.read_text()) if args.asset_hashes_file else None
        require(asset_hashes is None or isinstance(asset_hashes, dict), "expected asset hashes must be an object")
        authority = validate_review(json.loads(args.result.read_text()), project_id=args.project_id,
                                    run_id=args.run_id, revision=args.revision,
                                    input_hash=args.input_hash, asset_hashes=asset_hashes,
                                    require_paid=args.require_paid, require_paid_pass=args.require_paid_pass)
        print(json.dumps({"valid": True, "authority": authority,
                          "scope": "response_consistency_only_not_transport_authentication"}))
        return 0
    except (ValueError, OSError) as error:
        print(json.dumps({"valid": False, "error": str(error)}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
