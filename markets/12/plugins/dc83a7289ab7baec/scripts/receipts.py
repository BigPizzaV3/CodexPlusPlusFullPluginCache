"""File-based validation shared by local runners; no credentials or network calls."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def payload(value: dict) -> dict:
    if not isinstance(value, dict):
        raise ValueError("MCP result must be an object")
    if value.get("error") is not None or value.get("error_code") or value.get("isError") is True:
        raise ValueError("MCP reported an error; a read-back cannot turn it into a successful receipt")
    if "result" in value:
        return payload(value["result"])
    if isinstance(value.get("structuredContent"), dict):
        return payload(value["structuredContent"])
    if "content" in value and isinstance(value["content"], list):
        for item in value["content"]:
            if isinstance(item, dict) and item.get("type") == "text":
                try:
                    decoded = json.loads(item["text"])
                except (ValueError, TypeError):
                    continue
                if isinstance(decoded, dict):
                    return payload(decoded)
        raise ValueError("MCP response contains no structured JSON receipt")
    return value


def verify_translation(value: dict, expected_id: str | None = None,
                       language: str | None = None, operation_id: str | None = None) -> dict:
    result = payload(value)
    if result.get("persisted") is not True:
        raise ValueError("Translation persistence is unverified")
    for field in ("verification", "replyToVerification", "senderVerification"):
        if not isinstance(result.get(field), dict) or result[field].get("verified") is not True:
            raise ValueError(f"Translation {field} is unverified")
    target = result.get("writeOperation", {}).get("target", {})
    if expected_id is not None and str(target.get("id")) != str(expected_id):
        raise ValueError("Translation receipt identifies a different base message")
    if language is not None and (target.get("variant") or {}).get("language") != language:
        raise ValueError("Translation receipt identifies a different language")
    if operation_id is not None and result.get("replyToOperationId") != operation_id:
        raise ValueError("Translation receipt identifies a different logical operation")
    return result


def verify_count(value: dict) -> dict:
    result = payload(value)
    count = result.get("totalCount")
    if (type(count) is not int or count < 0
            or result.get("status", "COMPLETED") != "COMPLETED"):
        raise ValueError("Audience result is unavailable, pending or malformed; never treat it as zero")
    return {**result, "status": "COMPLETED"}


def verify_segment(value: dict, expected_id: str | None = None) -> dict:
    result = payload(value)
    segment_id = str(result.get("segmentId", ""))
    if (not segment_id.isdecimal() or int(segment_id) <= 0
            or (expected_id is not None and segment_id != str(expected_id))
            or result.get("commitStatus") in {"unknown", "not_committed", "failed"}
            or ("updated" in result and result["updated"] is not True)
            or result.get("readback") != "retrieved"):
        raise ValueError("Segment persistence/read-back is unverified; retain the destination and inspect before retrying")
    return result


def verify_workflow(value: dict, expected_id: int, created: bool = False) -> dict:
    result = payload(value)
    verification = result.get("verification")
    if result.get("workflowId") != expected_id:
        raise ValueError("Workflow receipt identifies a different destination")
    if (result.get("updated") is not True or not isinstance(verification, dict)
            or verification.get("verified") is not True
            or not isinstance(result.get("modelHash"), str) or not result["modelHash"]
            or result.get("commitStatus") in {"unknown", "not_committed", "failed"}):
        raise ValueError("Workflow save is unverified; inspect the retained destination before retrying")
    if created and verification.get("paused") is not True:
        raise ValueError("New workflow was not verified as paused")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=["translation", "count", "segment", "workflow"])
    parser.add_argument("--response", required=True, type=Path)
    parser.add_argument("--expected-id")
    parser.add_argument("--language")
    parser.add_argument("--operation-id")
    parser.add_argument("--created", action="store_true")
    args = parser.parse_args()
    try:
        value = json.loads(args.response.read_text())
        if args.kind == "workflow":
            if args.expected_id is None:
                raise ValueError("Workflow verification requires --expected-id")
            verify_workflow(value, int(args.expected_id), args.created)
        elif args.kind == "segment":
            verify_segment(value, args.expected_id)
        elif args.kind == "translation":
            verify_translation(value, args.expected_id, args.language, args.operation_id)
        else:
            verify_count(value)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Receipt verification failed: {exc}\n")
    print(json.dumps({"verified": True, "kind": args.kind}))


if __name__ == "__main__":
    main()
