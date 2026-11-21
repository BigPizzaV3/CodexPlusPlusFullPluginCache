"""Compatibility import for the Codex runtime."""

import sys

from .studio import canvas_sync as _implementation

sys.modules[__name__] = _implementation
