"""Compatibility import for the Codex runtime."""

import sys

from .studio import python_dependencies as _implementation

sys.modules[__name__] = _implementation
