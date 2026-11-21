#!/usr/bin/env python3
"""Prepare a partial profile_update and verify its merged read-back without network access."""
from __future__ import annotations

import argparse
from copy import deepcopy
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
from receipts import payload
from transfer import atomic_write


def pointer(parts):
    return "/" + "/".join(str(part).replace("~", "~0").replace("/", "~1") for part in parts)


def merge(current, changes, clears=(), parts=()):
    if not isinstance(changes, dict):
        if changes in (None, "", []) and pointer(parts) not in clears:
            raise ValueError(f"Explicit clear permission is required for {pointer(parts)}")
        return deepcopy(changes)
    result = deepcopy(current) if isinstance(current, dict) else {}
    for key, value in changes.items():
        result[key] = merge(result.get(key), value, clears, (*parts, key))
    return result


def profile(raw, organization_id):
    result = payload(raw)
    if str(result.get("orgId")) != str(organization_id) or not isinstance(result.get("brandkit"), dict):
        raise ValueError("Business Profile result is not bound to the selected organization")
    if result.get("error_code"):
        raise ValueError("Business Profile reported an error")
    return result["brandkit"]


def prepare(current, changes, clears=()):
    if not isinstance(changes, dict) or not changes:
        raise ValueError("Changes must be a nonempty partial profile object")
    document = {"brand": {}, **changes}
    if not isinstance(document["brand"], dict):
        raise ValueError("brand must be an object")
    expected = merge(current, document, clears)
    languages = expected.get("languages")
    voice_languages = expected.get("brand", {}).get("brandVoice", {}).get("defaultLanguages")
    if languages and voice_languages and languages != voice_languages:
        raise ValueError("Update languages and brand.brandVoice.defaultLanguages together")
    return document, expected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["prepare", "verify"])
    parser.add_argument("--current", type=Path, required=True)
    parser.add_argument("--organization-id", required=True)
    parser.add_argument("--changes", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--expected", type=Path, required=True)
    parser.add_argument("--clear", action="append", default=[])
    args = parser.parse_args()
    try:
        current = profile(json.loads(args.current.read_text()), args.organization_id)
        if args.command == "verify":
            expected = json.loads(args.expected.read_text())
            if current != expected:
                raise ValueError("Saved profile differs from the merge preview; inspect normalization and unrequested changes")
            print(json.dumps({"verified": True}))
        else:
            if not args.changes or not args.output:
                raise ValueError("prepare requires --changes and --output")
            document, expected = prepare(current, json.loads(args.changes.read_text()), args.clear)
            for file, value in ((args.output, document), (args.expected, expected)):
                atomic_write(file, (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode())
            print(json.dumps({"prepared": True, "persisted": False}))
    except (ValueError, OSError, TypeError) as exc:
        parser.exit(1, f"Profile check failed: {exc}\n")


if __name__ == "__main__":
    main()
