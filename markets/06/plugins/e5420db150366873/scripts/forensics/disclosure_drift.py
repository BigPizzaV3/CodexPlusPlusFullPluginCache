#!/usr/bin/env python3
"""Command wrapper for finance_core.disclosure_drift."""
from __future__ import annotations
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from finance_core import disclosure_drift

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: disclosure_drift.py '{JSON keyword arguments}'")
    print(json.dumps(disclosure_drift(**json.loads(sys.argv[1])), indent=2, sort_keys=True))
