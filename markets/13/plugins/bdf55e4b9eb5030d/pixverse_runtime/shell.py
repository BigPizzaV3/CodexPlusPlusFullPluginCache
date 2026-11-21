"""Compatibility import for the Codex runtime."""

import sys

from .studio import shell as _implementation

sys.modules[__name__] = _implementation
