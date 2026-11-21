"""Compatibility namespace for legacy Codex plugin commands."""

import os
import sys
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
os.environ.setdefault("PIXVERSE_AGENT_PLUGIN_ROOT", str(_root))
os.environ.setdefault("PIXVERSE_AGENT_RUNTIME_EXECUTABLE", str(_root / "scripts" / "pixverse-runtime"))
os.environ.setdefault("PIXVERSE_CLI_SOURCE", "codex-plugin")
_source_runtime = _root / "packages" / "runtime"
if _source_runtime.is_dir():
    sys.path.insert(0, str(_source_runtime))
