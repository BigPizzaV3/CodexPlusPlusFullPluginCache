#!/usr/bin/env python3
"""Command wrapper for finance_core.cash_conversion."""
from __future__ import annotations
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from finance_core import cash_conversion

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: cash_conversion.py '{JSON keyword arguments}'")
    print(json.dumps(cash_conversion(**json.loads(sys.argv[1])), indent=2, sort_keys=True))
