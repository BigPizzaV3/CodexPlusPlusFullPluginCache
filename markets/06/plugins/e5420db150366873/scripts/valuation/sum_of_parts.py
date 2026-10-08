#!/usr/bin/env python3
"""Command wrapper for finance_core.sum_of_parts."""
from __future__ import annotations
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from finance_core import sum_of_parts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: sum_of_parts.py '{JSON keyword arguments}'")
    print(json.dumps(sum_of_parts(**json.loads(sys.argv[1])), indent=2, sort_keys=True))
