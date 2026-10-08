#!/usr/bin/env python3
"""Fail closed on a metadata-execution manifest before any connector is invoked."""
import argparse
import hashlib
import json
from pathlib import Path
from execution_manifest import load_manifest


def main():
    parser = argparse.ArgumentParser(description="Validate a confirmed Dataverse execution manifest")
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    try:
        data, issues, digest = load_manifest(args.manifest)
    except (OSError, ValueError) as exc:
        data, issues, digest = {}, [str(exc)], None
    result = {"safeToInvokeConnector": not issues, "issues": issues, "manifestHash": digest,
              "writeApproved": data.get("writeApproved") is True}
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.as_json else ("PASS " if not issues else "BLOCKED ") + "; ".join(issues or [result["manifestHash"]]))
    raise SystemExit(0 if not issues else 1)


if __name__ == "__main__":
    main()
