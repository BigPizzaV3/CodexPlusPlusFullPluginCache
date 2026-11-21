"""Compatibility import for the Codex runtime."""

import sys

from .studio import internal_cli as _implementation

sys.modules[__name__] = _implementation
