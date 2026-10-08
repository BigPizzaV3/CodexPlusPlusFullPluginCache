#!/usr/bin/env python3
"""Command wrapper for finance_core.reverse_dcf_implied_growth."""
from __future__ import annotations
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from finance_core import reverse_dcf_implied_growth

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: reverse_dcf_implied_growth.py '{JSON keyword arguments}'")
    print(json.dumps(reverse_dcf_implied_growth(**json.loads(sys.argv[1])), indent=2, sort_keys=True))
