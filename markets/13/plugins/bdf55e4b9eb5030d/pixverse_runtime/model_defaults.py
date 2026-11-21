"""Compatibility import for the Codex runtime."""

import sys

from .studio import model_defaults as _implementation

sys.modules[__name__] = _implementation
