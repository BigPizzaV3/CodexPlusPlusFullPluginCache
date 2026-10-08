#!/usr/bin/env python3
"""Launch native-runtime E2E gates through their canonical import identity."""

from __future__ import annotations

import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))

import native_runtime  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(native_runtime.main(sys.argv[1:]))
