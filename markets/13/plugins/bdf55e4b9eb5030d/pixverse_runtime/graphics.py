"""Compatibility import for the Codex runtime."""

import sys

from .studio import graphics as _implementation

sys.modules[__name__] = _implementation
