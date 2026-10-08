#!/usr/bin/env python3
"""Launch the Meetings MCP through its canonical import identity."""

from __future__ import annotations

import sys
from pathlib import Path

if sys.version_info < (3, 10):
    raise SystemExit(
        "ChatGPT Meetings requires Python 3.10 or newer. Update the ChatGPT app or set "
        "CHATGPT_MEETINGS_PYTHON to a supported interpreter."
    )

# The sealed plugin runtime must not create bytecode beside attested sources.
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))

import meetings_mcp  # noqa: E402

if __name__ == "__main__":
    meetings_mcp.main()
