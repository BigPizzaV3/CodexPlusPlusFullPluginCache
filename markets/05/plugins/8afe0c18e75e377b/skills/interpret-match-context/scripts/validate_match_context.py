#!/usr/bin/env python3
"""Validate the current application AI payload using only the standard library."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate(payload: object) -> dict[str, object]:
    require(isinstance(payload, dict), "payload must be an object")
    require(set(payload) == {"match", "wiki"}, "payload must contain only match and wiki")
    match, wiki = payload["match"], payload["wiki"]
    require(isinstance(match, dict), "match must be an object")
    require(isinstance(wiki, dict), "wiki must be an object")
    required = {"id", "name", "age", "source", "language", "status", "createdAt",
                "messages", "details", "check_list", "summary", "ai_generations"}
    require(set(match) == required, f"match keys must be exactly {sorted(required)}")
    for key in ("id", "name", "source", "createdAt"):
        require(isinstance(match[key], str) and bool(match[key].strip()), f"match.{key} must be non-empty")
    require(match["language"] in {"lt", "en"}, "match.language is unsupported")
    require(match["status"] in {"active", "ghosted", "lost_interest", "cta", "liked_message"}, "match.status is unsupported")
    require(match["age"] is None or isinstance(match["age"], int) and match["age"] >= 18, "match.age must be null or >= 18")
    require(isinstance(match["summary"], str), "match.summary must be a string")
    require(isinstance(match["details"], dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in match["details"].items()), "match.details must map strings to strings")

    require(isinstance(match["messages"], list), "match.messages must be an array")
    timeline_ids: set[str] = set()
    for index, item in enumerate(match["messages"]):
        require(isinstance(item, dict), f"messages[{index}] must be an object")
        item_id = item.get("id")
        require(isinstance(item_id, str) and bool(item_id), f"messages[{index}].id is required")
        require(item_id not in timeline_ids, f"duplicate timeline ID: {item_id}")
        timeline_ids.add(item_id)
        kind = item.get("kind")
        require(kind in {"message", "ghosted", "lost_interest", "cta", "liked_message"}, f"messages[{index}].kind is unsupported")
        if kind == "message":
            require(item.get("author") in {"me", "her"}, f"messages[{index}].author is unsupported")
            require(isinstance(item.get("text"), str), f"messages[{index}].text must be a string")

    require(isinstance(match["check_list"], list), "match.check_list must be an array")
    checklist_ids: set[str] = set()
    for index, item in enumerate(match["check_list"]):
        require(isinstance(item, dict) and set(item) == {"id", "label", "answer"}, f"check_list[{index}] has invalid shape")
        require(all(isinstance(item[key], str) for key in item), f"check_list[{index}] values must be strings")
        require(item["id"] not in checklist_ids, f"duplicate checklist ID: {item['id']}")
        checklist_ids.add(item["id"])

    require(isinstance(match["ai_generations"], list), "match.ai_generations must be an array")
    require(set(wiki) == {"fields", "checklist"}, "wiki must contain only fields and checklist")
    require(isinstance(wiki["fields"], dict), "wiki.fields must be an object")
    require(isinstance(wiki["checklist"], dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in wiki["checklist"].items()), "wiki.checklist must map strings to strings")
    for path, explanation in wiki["fields"].items():
        require(isinstance(path, str) and isinstance(explanation, dict), f"wiki.fields.{path} must be an object")
        require(set(explanation) == {"description", "values"}, f"wiki.fields.{path} has invalid shape")
        require(isinstance(explanation["description"], str), f"wiki.fields.{path}.description must be a string")
        require(isinstance(explanation["values"], dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in explanation["values"].items()), f"wiki.fields.{path}.values must map strings to strings")
    return {"valid": True, "matchId": match["id"], "messageCount": len(match["messages"]), "checklistCount": len(match["check_list"])}


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: validate_match_context.py <payload.json>")
    try:
        result = validate(json.loads(Path(sys.argv[1]).read_text()))
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(json.dumps({"valid": False, "error": str(error)}, indent=2))
        raise SystemExit(1) from error
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
