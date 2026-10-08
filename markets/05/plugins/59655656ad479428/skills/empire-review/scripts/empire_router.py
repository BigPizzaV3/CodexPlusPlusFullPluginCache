#!/usr/bin/env python3
"""Stable CLI entry point for the Empire review runtime.

The marketplace scans each skill independently. Keep this entry point small and
place the implementation in the plugin-level scripts directory so expanding
routing and paid-response recovery cannot make the skill scanner time out.
"""

from __future__ import annotations

import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[3]
PLUGIN_SCRIPTS_ROOT = PLUGIN_ROOT / "scripts"
if str(PLUGIN_SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(PLUGIN_SCRIPTS_ROOT))

import empire_review_runtime as _runtime  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(_runtime.main())

# Preserve the historical import contract for tests and integrations that use
# `import empire_router`. Returning the runtime module also keeps monkeypatching
# deterministic because function globals and patched attributes share one module.
sys.modules[__name__] = _runtime
