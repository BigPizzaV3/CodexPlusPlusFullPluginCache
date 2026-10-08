#!/usr/bin/env python3
"""Command wrapper for finance_core.working_capital_metrics."""
from __future__ import annotations
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from finance_core import working_capital_metrics

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: working_capital_metrics.py '{JSON keyword arguments}'")
    print(json.dumps(working_capital_metrics(**json.loads(sys.argv[1])), indent=2, sort_keys=True))
