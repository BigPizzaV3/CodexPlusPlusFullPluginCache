"""Compatibility import for the Codex runtime."""

import sys

from .studio import state as _implementation

sys.modules[__name__] = _implementation
