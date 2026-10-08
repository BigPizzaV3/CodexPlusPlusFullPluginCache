#!/usr/bin/env python3
"""Command wrapper for finance_core.share_count_bridge."""
from __future__ import annotations
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from finance_core import share_count_bridge

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: share_count_bridge.py '{JSON keyword arguments}'")
    print(json.dumps(share_count_bridge(**json.loads(sys.argv[1])), indent=2, sort_keys=True))
