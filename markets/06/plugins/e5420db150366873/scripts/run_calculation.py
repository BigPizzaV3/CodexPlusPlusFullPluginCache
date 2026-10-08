#!/usr/bin/env python3
"""JSON command-line interface for finance_core functions."""
from __future__ import annotations
import argparse
import inspect
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import finance_core


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("function")
    parser.add_argument("json_args", help="JSON object containing keyword arguments")
    args = parser.parse_args()
    function = getattr(finance_core, args.function, None)
    if function is None or not inspect.isfunction(function) or function.__module__ != "finance_core":
        raise SystemExit(f"unknown finance_core function: {args.function}")
    result = function(**json.loads(args.json_args))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
